import logging

from ..common import DEFAULT_SCHEMA, FlatFileTools
from ..common.database import PostgresTools

DATASET_DIRECTORY = "/dataset"
LOGGER = logging.getLogger(__name__)
PREFIX_SEPARATOR = "_"


def load_data_from_csvs_into_postgres():
    required_tables = FlatFileTools.get_tables_by_prefix_separator(
        DATASET_DIRECTORY, PREFIX_SEPARATOR
    )
    for table in required_tables:
        LOGGER.info(f"Loading data for table:  {table}")
        data_files = FlatFileTools.get_csv_data_files_for_table(
            DATASET_DIRECTORY, table, PREFIX_SEPARATOR
        )
        PostgresTools.load_files_into_database(
            DEFAULT_SCHEMA, table, data_files
        )


if __name__ == "__main__":
    load_data_from_csvs_into_postgres()
