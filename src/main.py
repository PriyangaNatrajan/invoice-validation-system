from config import DATA_PATH
from data_loader import load_data
from data_cleaning import clean_data
from eda import eda
from validators import *
from outlier_detection import outliers
from report_generator import report_gen
def main():
    df = load_data(DATA_PATH)
    df = clean_data(df)
    prblms=[]
    prblms+=missing(df)
    prblms+=consistency(df)
    prblms+=subtotal(df)
    prblms+=total(df)
    prblms+=neg_values(df)
    prblms+=outliers(df, "qty")
    print("Sample issue:", prblms[0])
    print("Length of first issue tuple:", len(prblms[0]))

    report_gen(df, prblms)
if __name__ == "__main__":
    main()
    
