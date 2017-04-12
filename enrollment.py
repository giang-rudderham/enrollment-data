import sys
import pandas as pd
import re

# check if the file was executed from command line
if __name__ == "__main__":
    print("This also works!")

# read data    
data_enr = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")

# Find total enrollment
data_enr["total_enrollment"] = data_enr["TOT_ENR_M"] + data_enr["TOT_ENR_F"]

# Find sum of total enrollment column
all_enrollment = data_enr["total_enrollment"].sum()
print(all_enrollment)

# Compute sums of columns that break down enrollment by race and gender
##################################
# Get a list all column names
cols_list = list(data_enr.columns.values)
# Get a list of column names that start with SCH_ENR
enr_list = []
for i in cols_list:                                                 
    if re.match("^SCH_ENR_.", i) != None: 
        enr_list.append(i)
        
#print(len(cols_list))
#print(len(enr_list)) # have 20 column names
#print(enr_list)

# Only the first 14 column names are relevant
enr_list = enr_list[0:14] 
#print(enr_list) # have 14 column names

# Extract only the above 14 columns
new_data = data_enr[enr_list]
#print(new_data.shape)

# last step: calculate column sums
col_sums = new_data.sum(axis = 0)
#print(col_sums)

# Find % of enrollment for each race and gender
##########################
col_perc = col_sums / all_enrollment
print(col_perc)
print(col_perc.sum()) # should be 1