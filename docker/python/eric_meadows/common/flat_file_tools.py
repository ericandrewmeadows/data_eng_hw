import os
from glob import glob
from typing import List


class FlatFileTools(object):
    @classmethod
    def get_tables_by_prefix_separator(
        cls, data_directory, prefix_separator: str = "_"
    ) -> List[str]:
        potential_tables = [
            pt.split(prefix_separator)[0] for pt in os.listdir("/dataset")
        ]
        tables = set(potential_tables)
        return list(tables)

    @classmethod
    def get_csv_data_files_for_table(
        cls, dataset_directory: str, table: str, prefix_separator: str
    ) -> List[str]:
        data_files_glob = f"{table}{prefix_separator}*.csv"
        data_files = glob(os.path.join(dataset_directory, data_files_glob))
        return data_files
