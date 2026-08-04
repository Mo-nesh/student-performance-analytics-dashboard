import pandas as pd

print("Student Performance Analytics Dashboard")

df = pd.read_csv("data/student_performance.csv")

print(df.head())

print("\nSummary Statistics")
print(df.describe())
