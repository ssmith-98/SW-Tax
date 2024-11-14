import pandas as pd


df = pd.read_csv(r"C:\Users\smits\OneDrive - SW Accountants & Advisors Pty Ltd\Desktop\SW-Tax\USC Marking Analysis\IRM Data\IRM_AssessmentComponent_20240926.csv")


# DATA QUALITY

#1. Check for missing values

print(df.isnull().sum())