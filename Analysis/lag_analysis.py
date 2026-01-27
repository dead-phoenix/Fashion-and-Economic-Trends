import pandas as pd

df = pd.read_csv("Dataset/final_merged_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

econ_cols = ["Unemployment Rate (%)", "CPI_Index", "Seasonally Adjusted Turnover ($m)"]
fashion_cols = [c for c in df.columns if c not in econ_cols + ["Date", "Retail_Data_Available"]]

lags = [0, 3, 6, 9, 12]
results = []

for lag in lags:
    temp = df.copy()
    for col in econ_cols:
        temp[col] = temp[col].shift(lag)
    corr = temp[econ_cols + fashion_cols].corr()
    corr = corr.loc[econ_cols, fashion_cols].mean(axis=0)
    
    # Save each lag result as a row
    row = {"lag_months": lag}
    for c in fashion_cols:
        row[c] = corr[c]
    results.append(row)

lag_df = pd.DataFrame(results)
lag_df.to_csv("analysis_outputs/lag_analysis_results.csv", index=False)

print("Lag analysis saved")