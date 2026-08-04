import pandas as pd

def load_data():
    df = pd.read_csv("data/student_performance.csv")
    return df

if __name__ == "__main__":
    df = load_data()

    print("Student Performance Analytics Dashboard")
    print("--------------------------------------")

    print(df.head())

    print("\nDataset Summary\n")
    print(df.describe())
