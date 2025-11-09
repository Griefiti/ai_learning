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

temps = np.random.normal(loc=27, scale=3, size=1000)
plt.hist(temps)          # bins = 10 is default
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()

plt.hist(
    temps,
    bins=12,              # number of bins (more = finer)
    color='skyblue',
    edgecolor='black',
    alpha=0.8
)
plt.title("Temperature Distribution (Styled)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()

plt.hist(df["Sales"], bins=5, color='orange', edgecolor='black')
plt.title("Sales Value Distribution")
plt.xlabel("Sales ($)")
plt.ylabel("Frequency")
plt.show()

plt.hist(df["Profit"], bins=5, alpha=0.6, label="Profit")
plt.hist(df["Expenses"], bins=5, alpha=0.6, label="Expenses")
plt.title("Sales vs Expenses Distribution")
plt.xlabel("Amount ($)")
plt.ylabel("Frequency")
plt.legend()
plt.show()