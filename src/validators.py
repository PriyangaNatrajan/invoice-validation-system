from config import TOLERANCE
def missing(df):
    prblm=[]
    for c in df.columns:
        missing_r=df[df[c].isnull()].index
        for i in missing_r:
            prblm.append((i, f"Missing value in column {c}"))
    return prblm
def consistency(df):
    prblm=[]
    invalid=df[df['due_date']<df['invoice_date']]
    for i in invalid.index:
        prblm.append((i,'due date is before invoice date'))
    return prblm
def subtotal(df):
    prblm=[]
    calc=df['qty']*df['unit_price']
    diff=abs(calc-df['subtotal'])>TOLERANCE
    for i in df[diff].index:
        prblm.append((i,"subtotal mismatch"))
    return prblm
def total(df):
    prblm=[]
    expected=df['subtotal']+df['tax_amount']
    diff=abs(expected-df['total_amount'])>TOLERANCE
    for i in df[diff].index:
        prblm.append((i,'total amount is mismatched'))
    return prblm
def neg_values(df):
    prblm=[]
    invalid=df[df['qty']<0]
    for i in invalid.index:
        prblm.append((i,"negative quantity present"))
    return prblm 