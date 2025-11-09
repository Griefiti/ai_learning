import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
# === BASE PATH SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

file = "sales_data.csv"
FILE_PATH = os.path.join(DATA_DIR, file)

df = pd.read_csv(FILE_PATH)

plt.bar(df["Month"], df["Sales"], color="skyblue", edgecolor="black", linewidth=1.3)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Dollars($)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()

x = np.arange(len(df["Month"]))  # numeric positions [0,1,2,3,4,5]
width = 0.3                   # each bar width
plt.bar(x - width, df["Sales"], width, label="Sales")
plt.bar(x, df["Expenses"], width, label="Expenses")
plt.bar(x + width, df["Profit"], width, label="Profit")

plt.xticks(x, df["Month"])  # replace 0,1,2,... with "Jan","Feb",...
plt.title("With np.arange() — Properly Spaced Bars")
plt.legend()
plt.show()

plt.barh(df["Month"], df["Sales"], color="teal")
plt.title("Sales by Month (Horizontal)")
plt.xlabel("Sales ($)")
plt.ylabel("Month")
plt.show()