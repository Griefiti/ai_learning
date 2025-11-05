'''Concept 1 — import pandas as pd and df naming'''

import pandas as pd

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Temp_C": [30, 32, 28, 35, 31],
    "Rain_mm": [5, 0, 12, 0, 3]
}

df = pd.DataFrame(data)

print(df)
print()

'''Concept 2 — Inspecting Data (.head(), .tail(), .info(), .describe())'''

print(df.head(2)) # 5 is default, head is from the top
print(df.tail(2)) # tail is from the bottom
print()

print(df.info())  # supposedly a summary of the dataframe
print()

print(df.describe().round(2)) # summarizes count, mean, stdev, min, max, 25% 50% 75%.
print()                       # stdev is sample by default

print(df.shape)     # row, column
print(df.columns)
print()

'''Concept 3 — Accessing Columns & Rows in Pandas'''

print(df["Day"])    # bracket notation
print(df[["Temp_C","Rain_mm"]]) # double brackets for multiple columns
print(df.Temp_C)    # dot notation, quick but not safe
print()

#Accessing rows
print(df.loc[1])    # label-based but since my df is using default index, doesnt matter.    [row,column]
print(df.iloc[0])   # integer-based, iloc uses row position so even if label names are changed, very reliable
print()
print(df.loc[3,"Day"])  # can access cells
print(df.loc[4,["Day", "Temp_C"]])  # 5th row of both Day and Temp_C
print(df.loc[2:,"Rain_mm"])    #3rd to last row of Rain_mm
print(df.iloc[0,[1,2]]) # 1st row of second and third column

# so u can use .loc to access multiple rows in a single column, single row in multiple columns
# even one specific cell

'''Concept 4 — Filtering and Conditional Selection'''

hot_days = df[df["Temp_C"] > 31]
print(hot_days)
print()

warm_rainy_days = df[(df["Rain_mm"] >= 5) & (df["Temp_C"] <= 30)]
print(warm_rainy_days)
print()

T_days = df[df["Day"].str.startswith("T")]
U_days = df[df["Day"].str.contains("u")]
E_days = df[df["Day"].str.endswith("e")]
UP_days = df["Day"].str.upper()
len_days = df["Day"].str.len()
print(T_days)
print(U_days)
print(E_days)
print(UP_days)
print(len_days)
print()

lukewarm_days = df[(df["Temp_C"] >= 29) & (df["Temp_C"] <= 33)]
print(lukewarm_days)
      
next2_weekend = df[df["Day"].isin(["Mon", "Fri"])]
print(next2_weekend)
print()

'''Concept 5 — Adding & Modifying Columns in Pandas'''

df["Temp_F"] = df["Temp_C"] * 9/5 + 32
print(df)
df["Rainy_Day"] = df["Rain_mm"] > 0
print(df)
df["Weather_Type"] = df["Temp_C"].apply(lambda temp: "Hot" if temp > 32 else "Cool") 
print(df)

month_df = df.assign(
    Month = ["April", "May", "June", "July", "Augest"]
)
print(month_df)

df.drop(columns="Temp_F", inplace=True)
print(df)
df = df.rename(columns={"Temp_C": "Temperature_C"})
print(df)
df = df.drop(index=0)
print(df)
df = df.rename(index={1:"Day 2", 2:"Day 3"})
print(df)
print(df.loc["Day 2"])