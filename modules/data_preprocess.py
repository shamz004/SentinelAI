import pandas as pd
import glob

def load_dataset():
    files = glob.glob("dataset/*.csv")

    df_list = []

    for file in files:
        df = pd.read_csv(file)

        # normalize column names
        df = df.rename(columns={
            df.columns[0]: "text",
            df.columns[1]: "label"
        })

        df_list.append(df)

    final_df = pd.concat(df_list, ignore_index=True)
    return final_df