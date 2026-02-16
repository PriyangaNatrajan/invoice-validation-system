import json
from config import REPORT_PATH
def report_gen(df,prblm):
    report=[]
    for i,msg in prblm:
        report.append({"invoice_id":df.loc[i,"invoice_id"],"row_index":int(i),"issue":msg})
    with open(REPORT_PATH,"w") as f:
        json.dump(report,f,indent=4)
    print("report generated...")
    print("total issues found:",len(report))
