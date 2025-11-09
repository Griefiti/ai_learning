import pandas as pd
import matplotlib.pyplot as plt
import os
# === BASE PATH SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

file = "sales_data.csv"
FILE_PATH = os.path.join(DATA_DIR, file)

df = pd.read_csv(FILE_PATH)

columns = ["Profit", "Expenses", "Sales"]
color = ["green", "red", "blue"]
marker = ["^", "v", "x"]
linestyle = [":", "--", "-."]

plt.figure("Monthly Sales Report", figsize=(7,5))
for c, co, m, l in zip(columns,color, marker, linestyle):
    plt.plot(df["Month"], df[c], color=co, marker=m, linestyle=l, label=c)

plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold")
plt.xlabel("Month",fontsize=12)
plt.ylabel("Sales ($)",fontsize=12)
plt.legend(loc="best")
plt.grid(True)
plt.show()