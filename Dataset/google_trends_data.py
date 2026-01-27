from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

COUNTRY = "AU"
TIMEFRAME = "2010-01-01 2024-12-31"

KEYWORDS = [
    "luxury",
    "quiet luxury",
    "silent luxury",
    "minimalist fashion",
    "timeless basics",
    "capsule wardrobe",
    "thrift store",
    "second hand clothing",
    "vintage clothing",
    "short skirts",
    "mini skirts",
    "fast fashion",
    "statement pieces"
]

pytrends = TrendReq(hl="en-US", tz=360)


def fetch_trends(keyword):
    pytrends.build_payload([keyword], cat=0, timeframe=TIMEFRAME, geo=COUNTRY, gprop="")
    data = pytrends.interest_over_time()
    if data.empty:
        print(f"No data for {keyword}")
        return None
    data = data.drop(columns=["isPartial"])
    data = data.rename(columns={keyword: keyword.replace(" ", "_")})
    return data

# Fetch and merge all keywords
all_data = None
for kw in KEYWORDS:
    df = fetch_trends(kw)
    if df is not None:
        if all_data is None:
            all_data = df
        else:
            all_data = all_data.join(df, how="outer")

#clean
all_data = all_data.reset_index()
all_data = all_data.rename(columns={"date": "Date"})
all_data["Date"] = pd.to_datetime(all_data["Date"])
all_data = all_data.sort_values("Date")

# save
all_data.to_csv("fashion_trends_au_2010_2024.csv", index=False)

print("Saved fashion trends data!")