import pandas as pd
import numpy as np
import os
df = ""
summary = pd.DataFrame()
# === BASE PATH SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

file = "HistoricalDailyWeatherRecords_sg.csv"
FILE_PATH = os.path.join(DATA_DIR, file)

#--------------------------------
# FILE HANDLING
#--------------------------------
def ensure_file_exist():
    try:
        if not os.path.exists(FILE_PATH):
            open(file, "a").close()
            print(f"Missing file created: {file}")
    except FileNotFoundError:
        print("File not Found.")


def load_data():
    global df
    print("Loading data...")
    df = pd.read_csv(FILE_PATH, na_values=["NA", "N/A", "na", "--", " "])
    n = len(df)

    columns = [c for c in df if df[c].isnull().sum() < n/6]
    rows = [i for i in range(n) if df.iloc[i].isnull().sum() > len(columns) // 2]
    df = df[columns]
    df = df.drop(index= rows)
    
    if sum(df.isnull().sum()) > 0:
        print("Missing data detected in column(s):")
        for c in [c for c in df if df[c].isnull().sum() > 0]:
            print(f"{df.columns.get_loc(c) + 1}) {c:<20}: {df[c].isnull().sum():>2}")

        print("\nAutomatically filling in missing data...")
        df = df.fillna({
            "daily_rainfall_total": 0,
            "mean_temperature"    :df["mean_temperature"].mean().round(1),
            "maximum_temperature" :df["maximum_temperature"].interpolate(),
            "minimum_temperature" :df["minimum_temperature"].interpolate(),
            "max_wind_speed"      :df["max_wind_speed"].interpolate()
        })

    print("Dataset loaded successfully.")


def save_data():
    global summary
    pos = file.find(".")
    name = file[:pos]
    summary_name = name + "_summary.csv"
    summary_path = os.path.join(DATA_DIR, summary_name)
    summary.to_csv(summary_path, index=True)
    print("Summary saved successfully")
#--------------------------------
# CALCULATIONS
#--------------------------------
def analyze(chosen_c):
    global df, summary
    arr = df[chosen_c].to_numpy()
    print("\n== {} ==".format(chosen_c))
    print("{:<6}: {:>6}".format('Mean'  , np.mean(arr).round(2)))
    print("{:<6}: {:>6}".format('Median', np.median(arr)))
    print("{:<6}: {:>6}".format('Stdev' , np.std(arr, ddof=1).round(2)))
    print("{:<6}: {:>6}".format('Var'   , np.var(arr).round(2)))
    print("{:<6}: {:>6}".format('Min'   , np.min(arr)))
    print("{:<6}: {:>6}".format('Max'   , np.max(arr)))

    save = input(f"\nWould you like to save {chosen_c} to a summary(yes/no)? ").strip().lower()
    if save == "yes":
        if chosen_c not in summary:
            summary[chosen_c] = (
                np.mean(arr).round(2),
                np.median(arr),
                np.std(arr, ddof=1).round(2),
                np.var(arr).round(2),
                np.min(arr),
                np.max(arr)
            )
            summary = summary.rename(index={
                0:'Mean',
                1:'Median',
                2:'Stdev',
                3:'Var',
                4:'Min',
                5:'Max'
            })
            print(f"{chosen_c} saved successfully.")
        else:
            print(f"Already saved {chosen_c}, skipping..")

#--------------------------------
# MAIN MENU
#--------------------------------
def main_menu():
    global df
    while True:
        columns = [c for c in df if df[c].dtype == "float64"]
        n = len(columns)

        print("\n=========== MAIN MENU ===========")
        for i, c in enumerate(columns,1):
            print(f"Option {i}: {c}")
        print(f"Option {n+1}: Exit")
        choice = input("Please select an option to analyze: ").strip()

        if not choice or not choice.isdigit():
            print("\nInvalid Input. Try again."); continue
        choice = int(choice)
        if not (1 <= choice <= n+1):
            print(f"\nPlease enter a number from (1 - {n+1})."); continue
        if (1 <= choice <= n):
            analyze(columns[choice - 1])
        elif choice == n+1:
            print("\nExitting program.."); break

def main():
    ensure_file_exist()
    load_data()
    main_menu()
    save_data()

main()
