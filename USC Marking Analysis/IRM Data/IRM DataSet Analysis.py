import pandas as pd


import pandas as pd

# Specify a different encoding
df = pd.read_csv(r"C:\Users\smits\OneDrive - SW Accountants & Advisors Pty Ltd\Desktop\SW-Tax\USC Marking Analysis\IRM Data\IRM_AssessmentComponent_20240926.csv", encoding='ISO-8859-1')

# DATA QUALITY

#1. Check for missing values

print("Number of missing values by column: ")
print(df.isnull().sum())


#2. Check for duplicates 

print("Number of duplicated rows: ")
print(df.duplicated().sum())


# DATA STRUCTURE AND TYPES

#check the shape of the data
print("Data set shape No. Rows : No. Columns ")
print(df.shape)

#check the data types by column
print("Data Types by Column: ")
print(df.dtypes)

#Return the number of each data type
print("Number of columns by each data type: ")
print(df.dtypes.value_counts())