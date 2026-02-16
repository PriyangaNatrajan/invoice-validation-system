import pandas as pd
def load_data(p):
    try:
        df=pd.read_csv(p)
        return df
    except Exception as e:
        raise Exception("error with loading data")