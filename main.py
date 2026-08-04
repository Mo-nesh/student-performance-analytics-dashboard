import pandas as pd

def load_data():
    """Load student performance dataset."""
    return pd.read_csv("data/student_performance.csv")


def main():
    print("=" * 50)
    print("Student Performance Analytics Dashboard")
    print("=" * 50)

    df = load_data()

    print("\nDataset Preview:")
    print(df.head())

    print("\nDataset Information:")
    print(df.info())

    print("\nSummary Statistics:")
    print(df.describe())


if __name__ == "__main__":
    main()
