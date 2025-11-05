'''Concept 6 — NumPy Integration with Pandas'''
import pandas as pd
import numpy as np

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Temp_C": [30, 32, 28, 36, 31],
    "Rain_mm": [5, 0, 12, 0, 3]
}

df = pd.DataFrame(data)
temp_arr = df["Temp_C"].to_numpy()

print("Mean: ",np.mean(temp_arr))
print("Median: ",np.median(temp_arr))
print("Stdev: ",np.std(temp_arr).round(2))
print("Var: ",np.var(temp_arr).round(2))
print("Min: ",np.min(temp_arr))
print("Max: ",np.max(temp_arr))
print("Sum: ",np.sum(temp_arr))

df["Temp_Squared"] = np.power(df["Temp_C"], 2) # df.Temp_C ** 2
df["Temp_Square_rooted"] = np.power(df["Temp_C"], 1/2).round(2)
df["Temp_Deviation"] = df["Temp_C"] - np.mean(df["Temp_C"])
print(df)

df["Category"] = np.where(df.Temp_Deviation > 0,"HOT", "COLD")
print(df)