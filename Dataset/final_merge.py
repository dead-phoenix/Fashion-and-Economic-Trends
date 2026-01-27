import pandas as pd

# load
econ = pd.read_csv("Dataset/master_economic_dataset.csv")
fashion = pd.read_csv("Dataset/fashion_trends_au_2010_2024.csv")

# convert Date to datetime
econ["Date"] = pd.to_datetime(econ["Date"])
fashion["Date"] = pd.to_datetime(fashion["Date"])

# merge
df = pd.merge(econ, fashion, on="Date", how="inner")

# save
df.to_csv("Dataset/final_merged_dataset.csv", index=False)
print("Merged dataset saved.")
