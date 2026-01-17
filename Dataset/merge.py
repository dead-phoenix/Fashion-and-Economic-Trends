import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

unemp = pd.read_csv(os.path.join(BASE_DIR, "unemployment_cleaned.csv"))
cpi = pd.read_csv(os.path.join(BASE_DIR, "cpi_monthly_cleaned.csv"))
retail = pd.read_csv(os.path.join(BASE_DIR, "retail_sales_cleaned.csv"))

merged = unemp.merge(cpi, on="Date", how="outer")
merged = merged.merge(retail, on="Date", how="left")

# Fill missing retail values with 0
merged["Retail_Data_Available"] = merged["Retail_Data_Available"].fillna(False)
merged["Seasonally Adjusted Turnover ($m)"] = merged["Seasonally Adjusted Turnover ($m)"].fillna(0)

merged = merged.sort_values("Date")
merged.to_csv(os.path.join(BASE_DIR, "master_economic_dataset.csv"), index=False)

print("Master dataset created successfully.")
