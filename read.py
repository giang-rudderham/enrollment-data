import sys
import pandas as pd

if __name__ == "__main__":
    print("This works!")

contents = pd.read_csv("data/CRDC2013_14content.csv")
print(contents.head())
print(contents.columns.values)