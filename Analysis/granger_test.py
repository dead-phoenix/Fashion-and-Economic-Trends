import pandas as pd
from statsmodels.tsa.stattools import grangercausalitytests

df = pd.read_csv("Dataset/final_merged_dataset.csv", parse_dates=["Date"])
df = df.sort_values("Date").set_index("Date")

cols_needed = [
    "Unemployment Rate (%)",
    "CPI_Index",
    "Seasonally Adjusted Turnover ($m)",
    "quiet_luxury",
    "fast_fashion"
]

df_gc = df[cols_needed].dropna()

def run_granger_test(df, x, y, max_lag):
    """
    Tests whether x Granger-causes y
    """
    test_df = df[[y, x]]
    results = grangercausalitytests(test_df, maxlag=max_lag, verbose=False)

    p_values = {
        lag: results[lag][0]["ssr_ftest"][1]
        for lag in range(1, max_lag + 1)
    }

    return pd.Series(p_values, name=f"{x} → {y}")

ff_unemp = run_granger_test(df_gc, "Unemployment Rate (%)", "fast_fashion", 12)
ff_cpi = run_granger_test(df_gc, "CPI_Index", "fast_fashion", 12)

ql_unemp = run_granger_test(df_gc, "Unemployment Rate (%)", "quiet_luxury", 48)
ql_cpi = run_granger_test(df_gc, "CPI_Index", "quiet_luxury", 48)

granger_results = pd.concat(
    [ff_unemp, ff_cpi, ql_unemp, ql_cpi],
    axis=1
)

granger_results.to_csv("analysis_outputs/granger_results_selected.csv")