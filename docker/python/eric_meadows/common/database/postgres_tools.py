import sys
import traceback
from io import StringIO
from typing import Dict, List

import pandas as pd
import psycopg2

from ...queries import TABLE_DATE_COLUMNS, TEMPLATES
from ..common import (
    DEFAULT_DATABASE,
    DEFAULT_HOST,
    DEFAULT_PASSWORD,
    DEFAULT_POTENTIAL_NULL_COLUMNS,
    DEFAULT_USER,
)
from ..data_frame_tools import DataFrameTools
from .database_tools import DatabaseTools
from .dialect_mapping import DIALECT_MAPPING, PANDAS


class PostgresTools(DatabaseTools):
    def __init__(
        self,
        host: str = DEFAULT_HOST,
        database: str = DEFAULT_DATABASE,
        user: str = DEFAULT_USER,
        password: str = DEFAULT_PASSWORD,
        *args,
        **kwargs,
    ):
        super(PostgresTools, self).__init__(*args, **kwargs)
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = psycopg2.connect(
            host=self.host,
            dbname=self.database,
            user=self.user,
            password=self.password,
        )
        self.dataframe_tools = DataFrameTools()

    def _ensure_schema_present(self, schema: str):
        query_params = dict(schema=schema)
        query = self.load_jinja_query_template(
            TEMPLATES["CREATE_SCHEMA_IF_NOT_EXISTS"], query_params
        )
        self._run_query(query)

    def _drop_and_create_table_sql(
        self,
        database: str,
        table: str,
        dialect: str,
        schema_map: Dict[str, str],
    ) -> str:
        dialect_map = DIALECT_MAPPING[dialect]
        postgres_table_name = f"{database}.{table}"

        query_params = dict(
            postgres_table_name=postgres_table_name,
            mapping=dialect_map,
            schema_map=schema_map,
        )
        query_sql = self.load_jinja_query_template(
            TEMPLATES["DROP_AND_CREATE_TABLE_WITH_SCHEMA"], query_params
        )
        return query_sql

    def _drop_and_create_table(
        self, schema: str, table: str, dialect: str, schema_map: Dict[str, str]
    ):
        query = self._drop_and_create_table_sql(
            schema, table, dialect, schema_map
        )
        self._run_query(query)

    def _get_file_buffer_without_null_bytes(
        self,
        data_file: str,
        potential_null_columns: List[str] = DEFAULT_POTENTIAL_NULL_COLUMNS,
    ):
        writeable_csv_buffer = StringIO()
        pd.read_csv(data_file).dropna(subset=potential_null_columns).to_csv(
            writeable_csv_buffer, index=False, header=False
        )
        writeable_csv_buffer.seek(0)
        return writeable_csv_buffer

    def _load_file_into_table(
        self, schema: str, table: str, data_file: str, separator=","
    ):
        cursor = self.conn.cursor()
        writeable_csv_buffer = self._get_file_buffer_without_null_bytes(
            data_file
        )
        try:
            cursor.copy_from(
                writeable_csv_buffer,
                f"{schema}.{table}",
                sep=separator,
                null="",
            )
            self.conn.commit()
        except Exception as err:
            traceback.print_exc(file=sys.stdout)
            raise err
        finally:
            writeable_csv_buffer.close()
            cursor.close()

    def _run_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def load_files_into_database(
        self,
        schema: str,
        table: str,
        data_files: List[str],
        dialect: str = PANDAS,
    ):
        first_data_file = data_files[0]
        df = self.dataframe_tools.get_typed_dataframe_from_file(
            first_data_file, TABLE_DATE_COLUMNS.get(table, [])
        )
        schema_map = self.dataframe_tools.get_dtypes_dict_from_typed_dataframe(
            df
        )

        self._ensure_schema_present(schema)

        self._drop_and_create_table(schema, table, dialect, schema_map)
        for data_file in data_files:
            self._load_file_into_table(schema, table, data_file)
