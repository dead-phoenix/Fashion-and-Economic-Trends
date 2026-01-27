import pandas as pd

df = pd.read_csv("Dataset/final_merged_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Event period
covid = df[(df["Date"] >= "2020-01-01") & (df["Date"] <= "2021-12-31")]

# Save event data
covid.to_csv("analysis_outputs/covid_period_data.csv", index=False)

print("Event period data saved.")
