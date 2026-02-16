import matplotlib.pyplot as plt
import seaborn as sns
def eda(df):
    print("shape:",df.shape)
    print("missing values:",df.isnull().sum())
    print("duplicate entries:",df.duplicated().sum())
    print(" statistical summary ")
    print(df.describe())
    invalid_date = (df['due_date']<df['invoice_date']).sum()
    print("invalid date entries:",invalid_date)
    plt.figure()
    sns.histplot(df['total_amount'])
    plt.title("total amount distribution")
    plt.show()
    plt.figure()
    sns.histplot(df['qty'],kde=True)
    plt.title("quantity distribution")
    plt.show()
    plt.figure()
    sns.boxplot(x=df['qty'])
    plt.title("quantity boxplot")
    plt.show()
    num_colmns=['qty','unit price','subtotal','total amount','tax rate','tax amount']
    for c in num_colmns:
        plt.figure()
        sns.scatterplot(x=df[c],y=df['total_amount'])
        plt.title(c,"vs total amount")
        plt.show()
