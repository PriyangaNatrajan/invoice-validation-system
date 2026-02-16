import pandas as pd
def clean_data(df):
    df.columns=df.columns.str.strip().str.lower()
    df['invoice_date']=pd.to_datetime(df['invoice_date'],errors='coerce')
    df['due_date']=pd.to_datetime(df['due_date'],errors='coerce')
    num_colmn=['qty','unit_price','subtotal','total_amount','tax_rate','tax_amount']
    for c in num_colmn:
        df[c]=pd.to_numeric(df[c],errors='coerce')
    return df
















