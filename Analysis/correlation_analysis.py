import pandas as pd
import os
if not os.path.exists("analysis_outputs"):
    os.makedirs("analysis_outputs")

df = pd.read_csv("Dataset/final_merged_dataset.csv")

econ_cols = ["Unemployment Rate (%)", "CPI_Index", "Seasonally Adjusted Turnover ($m)"]
fashion_cols = [c for c in df.columns if c not in econ_cols + ["Date", "Retail_Data_Available"]]

corr_matrix = df[econ_cols + fashion_cols].corr()

# correlations between economic and fashion
corr = corr_matrix.loc[econ_cols, fashion_cols]

# Save to CSV
corr.to_csv("analysis_outputs/correlation_matrix.csv")

print("Correlation matrix saved")