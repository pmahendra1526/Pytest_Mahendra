import pandas as pd


def convert_column_datatypes(df:pd.DataFrame):
    # print("In Covert Function")
    print(list(df.columns))
    # print(df.values)
    if "DATA_TYPE" in df.columns:
        df.loc[df["DATA_TYPE"] == "NUMBER", "DATA_TYPE"] = 'int'
        df.loc[df["DATA_TYPE"] == "VARCHAR2", "DATA_TYPE"] = 'varchar'
    if "IS_NULLABLE" in df.columns:
        df.loc[df["IS_NULLABLE"] == "Y", "IS_NULLABLE"] = 'YES'
        df.loc[df["IS_NULLABLE"] == "N", "IS_NULLABLE"] = 'NO'
    # print(df)
    return df
