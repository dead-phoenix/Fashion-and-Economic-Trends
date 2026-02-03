import pandas as pd
import numpy as np
from scipy.stats import zscore

# Load merged dataset
df = pd.read_csv("Dataset/final_merged_dataset.csv", parse_dates=["Date"])
df = df.sort_values("Date")

# Economic variables
econ_vars = [
    "Unemployment Rate (%)",
    "CPI_Index",
    "Seasonally Adjusted Turnover ($m)"
]

# Fashion trend variables
fashion_vars = [
    "luxury",
    "quiet_luxury",
    "minimalist_fashion",
    "timeless_basics",
    "capsule_wardrobe",
    "thrift_store",
    "second_hand_clothing",
    "vintage_clothing",
    "short_skirts",
    "mini_skirts",
    "fast_fashion",
    "statement_pieces"
]

MAX_LAG = 48
results = []

# Standardize variables
df_std = df.copy()
for col in econ_vars + fashion_vars:
    df_std[col] = zscore(df_std[col], nan_policy="omit")

# Cross-correlation
for econ in econ_vars:
    for fashion in fashion_vars:
        for lag in range(0, MAX_LAG + 1):
            corr = df_std[econ].corr(df_std[fashion].shift(lag))
            results.append({
                "Economic_Variable": econ,
                "Fashion_Trend": fashion,
                "Lag_Months": lag,
                "Cross_Correlation": corr
            })

ccf_df = pd.DataFrame(results)

# Save full results
ccf_df.to_csv("cross_correlation_full.csv", index=False)

# Extract peak absolute correlation per pair
peak_corr = (
    ccf_df
    .dropna()
    .assign(abs_corr=lambda x: x["Cross_Correlation"].abs())
    .sort_values("abs_corr", ascending=False)
    .groupby(["Economic_Variable", "Fashion_Trend"])
    .first()
    .reset_index()
    .drop(columns="abs_corr")
)

peak_corr.to_csv("analysis_outputs/cross_correlation_peaks.csv", index=False)

print("Cross-correlation analysis completed")
