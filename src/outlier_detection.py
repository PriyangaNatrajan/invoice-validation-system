def outliers(df, col):
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    lower=q1-1.5*iqr
    upper=q3+1.5*iqr
    outliers=df[(df[col] < lower)|(df[col] > upper)]
    prblm=[]
    for i in outliers.index:
        prblm.append((i,f"outlier detected in {col}"))
    return prblm
