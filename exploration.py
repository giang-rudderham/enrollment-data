import sys
import pandas as pd

if __name__ == "__main__":
    print("This works too!")
    
data = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
# Count unique values in 2 columns
print(data["JJ"].value_counts())
print(data["SCH_STATUS_MAGNET"].value_counts())

# make table: count total number of males and females in column JJ
table1 = pd.pivot_table(data, values = ["TOT_ENR_M", "TOT_ENR_F"], index = "JJ", aggfunc = "sum")
# make table: count total number of males and females in column SCH_STATUS_MAGNET
table2 = pd.pivot_table(data, values = ["TOT_ENR_M", "TOT_ENR_F"], index = "SCH_STATUS_MAGNET", aggfunc = "sum")
# Note columns JJ and SCH_STATUS_MAGNET have only Yes and No as values

print(table1)
print(table2)