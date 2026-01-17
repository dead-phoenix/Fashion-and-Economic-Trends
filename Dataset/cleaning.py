import pandas as pd
import os

#loading datasets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UNEMP_FILE = os.path.join(BASE_DIR, "unemployment.csv")
CPI_FILE = os.path.join(BASE_DIR, "cpi.csv")
RETAIL_FILE = os.path.join(BASE_DIR, "retail_sales.csv")

#cleaning unemployment csv
unemp = pd.read_csv(UNEMP_FILE)

def clean_unemployment_value(val):
    if isinstance(val, str) and "," in val:
        nums = [float(x.strip()) for x in val.split(",")]
        return sum(nums) / len(nums)
    return float(val)

unemp["Unemployment Rate (%)"] = (
    unemp["Unemployment Rate (%)"]
    .apply(clean_unemployment_value)
    .round(2)
)

unemp["Date"] = pd.to_datetime(
    unemp["Month"] + " " + unemp["Year"].astype(str),
    format="%B %Y"
)

unemp = unemp[["Date", "Unemployment Rate (%)"]].sort_values("Date")

unemp.to_csv(os.path.join(BASE_DIR, "unemployment_cleaned.csv"), index=False)

#cleaning cpi csv
cpi = pd.read_csv(CPI_FILE)

# Rename column
cpi.rename(columns={"CPI index": "CPI_Index"}, inplace=True)

# Parse Date
cpi["Date"] = pd.to_datetime(cpi["Date"])

# Sort oldest to newest
cpi = cpi.sort_values("Date")

# Resample monthly and forward-fill
cpi_monthly = cpi.set_index("Date").resample("MS").ffill()

# Add Jan-Feb 2010 by reindexing
full_range = pd.date_range(start="2010-01-01", end=cpi_monthly.index.max(), freq="MS")

cpi_monthly = cpi_monthly.reindex(full_range).ffill().bfill()

# Reset index
cpi_monthly = cpi_monthly.reset_index().rename(columns={"index": "Date"})

cpi_monthly.to_csv(os.path.join(BASE_DIR, "cpi_monthly_cleaned.csv"), index=False)

#cleaning retail sales csv
retail = pd.read_csv(RETAIL_FILE)

retail["Date"] = pd.to_datetime(
    retail["Month"] + " " + retail["Year"].astype(str),
    format="%B %Y"
)

retail = retail[["Date", "Seasonally Adjusted Turnover ($m)"]].sort_values("Date")
retail["Retail_Data_Available"] = retail["Seasonally Adjusted Turnover ($m)"].notna()

retail.to_csv(os.path.join(BASE_DIR, "retail_sales_cleaned.csv"), index=False)

print("All datasets cleaned and saved successfully.")