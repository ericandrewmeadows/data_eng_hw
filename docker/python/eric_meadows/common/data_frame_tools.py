from typing import List

import pandas as pd
from pandas import DataFrame


class DataFrameTools(object):
    @classmethod
    def get_typed_dataframe_from_file(
        cls, data_file: str, date_columns: List[str]
    ):
        df = pd.read_csv(data_file, parse_dates=date_columns)
        return df

    @classmethod
    def get_dtypes_dict_from_typed_dataframe(cls, typed_df: DataFrame):
        dtypes_dict = typed_df.dtypes.to_dict()
        for key, value in dtypes_dict.items():
            dtypes_dict[key] = str(value).upper()
        return dtypes_dict
