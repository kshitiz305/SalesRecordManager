import os
import warnings

import pandas as pd

warnings.simplefilter(action='ignore', category=FutureWarning)


class ColumnException(Exception):
    def __int__(self, message):
        print(message)


master_df = pd.DataFrame()
directory_name = "sales_records"


class ConcatCsv():
    def __init__(self, directory_name):
        self.master_df = pd.DataFrame()
        self.directory_name = directory_name

    def concating_csvs(self) -> pd.DataFrame:
        for file in os.listdir(self.directory_name):
            if os.path.splitext(file)[1] in [".json"]:
                try:
                    df1 = pd.read_json(f"{self.directory_name}/{file}")
                    if self.master_df.shape[0] == 0:
                        self.master_df = self.master_df.append(df1, True)
                    else:
                        if self.master_df.columns.difference(df1.columns).empty == True:
                            self.master_df = self.master_df.append(df1, True)
                        else:
                            raise ColumnException(f"Columns of {file} are not equal to the other columns in main file")
                except ColumnException as exe:
                    print(exe)
                    continue

        return self.master_df


if __name__ == "__main__":
    final_df = ConcatCsv("sales_records").concating_csvs()
    final_df.to_csv("Final_csv.csv")
