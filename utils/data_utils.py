import pandas as pd
import duckdb

def save_csv(df, path):
    df.to_csv(path, index=False)
    return path

def load_csv(path):
    return pd.read_csv(path)

def save_json(df, path):
    df.to_json(path, orient="records", indent=2, force_ascii=False)
    return path

def load_json(path):
    return pd.read_json(path)

def save_parquet_no_pyarrow(df, path):
    con = duckdb.connect()
    con.register("df_view", df)
    con.execute(f"COPY df_view TO '{path}' (FORMAT PARQUET)")
    con.close()
    return path

def load_parquet_no_pyarrow(path):
    return duckdb.query(f"SELECT * FROM '{path}'").to_df()
