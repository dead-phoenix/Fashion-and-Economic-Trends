import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("analysis_outputs"):
    os.makedirs("analysis_outputs")

df = pd.read_csv("Dataset/final_merged_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

keywords = [
    "luxury",
    "quiet_luxury",
    "minimalist_fashion",
    "thrift_store",
    "mini_skirts",
]

for kw in keywords:
    plt.figure(figsize=(14, 5))
    plt.plot(df["Date"], df[kw], linewidth=2)
    
    # Plot details
    plt.title(f"Search Trend Over Time: {kw.replace('_', ' ').title()}", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Search Interest (0-100)", fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add vertical lines for major events
    plt.axvline(pd.to_datetime("2020-03-01"), color="red", linestyle="--", alpha=0.5)
    plt.text(pd.to_datetime("2020-03-01"), 90, "COVID Start", rotation=90, color="red")
    
    plt.axvline(pd.to_datetime("2011-01-01"), color="orange", linestyle="--", alpha=0.5)
    plt.text(pd.to_datetime("2011-01-01"), 90, "Post-Global Crisis", rotation=90, color="orange")
    
    # Save plot
    plt.savefig(f"analysis_outputs/{kw}_trend_plot.png", dpi=300, bbox_inches="tight")
    plt.close()

print("Trend plots saved")