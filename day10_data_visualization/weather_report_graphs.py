import pandas as pd
import matplotlib.pyplot as plt
import os
df = ""
# === BASE PATH SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

file = "HistoricalDailyWeatherRecords_sg.csv"
FILE_PATH = os.path.join(DATA_DIR, file)

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
    
    df = df.fillna({
        "daily_rainfall_total": 0,
        "mean_temperature"    :df["mean_temperature"].mean().round(1),
        "maximum_temperature" :df["maximum_temperature"].interpolate(),
        "minimum_temperature" :df["minimum_temperature"].interpolate(),
        "max_wind_speed"      :df["max_wind_speed"].interpolate()
    })
    print("Dataset loaded successfully.")

def graph(chosen_c):
    if chosen_c.endswith("d"): x = "km/h"
    elif chosen_c.endswith("e"): x = "Degree'C"
    else: x = "millimeter"
    format_c = chosen_c.replace("_"," ").capitalize()
    filename = "Distribution of " + format_c
    bins = int(input("Bins (press Enter for default 12): ") or 12)
    
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(format_c)
    ax.hist(df[chosen_c], bins=bins, color="coral", edgecolor="black", alpha=0.8)

    plt.title(filename, fontsize=13, fontweight="bold")
    plt.xlabel(x)
    plt.ylabel("Frequency")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.show()

    save = input("Save figure? (y/n): ").lower()
    if save == "y":
        PLOT_DIR = os.path.join(DATA_DIR, "plots")
        os.makedirs(PLOT_DIR, exist_ok=True)
        filepath = os.path.join(PLOT_DIR,chosen_c) + ".png"
        if os.path.exists(filepath):
            print(f"Already saved {filename}, skipping..")
        else:
            fig.savefig(filepath, dpi=300, bbox_inches="tight")


def main_menu():
    global df
    while True:
        columns = df.select_dtypes(include='number').columns
        n = len(columns)

        print("\n=========== MAIN MENU ===========")
        for i, c in enumerate(columns,1):
            print(f"Option {i}: {c}")
        print(f"Option {n+1}: Exit")
        choice = input("Please select an option to graph: ").strip()

        if not choice or not choice.isdigit():
            print("\nInvalid Input. Try again."); continue
        choice = int(choice)
        if not (1 <= choice <= n+1):
            print(f"\nPlease enter a number from (1 - {n+1})."); continue
        if (1 <= choice <= n):
            graph(columns[choice - 1])
        elif choice == n+1:
            print("\nExitting program.."); break
        
def main():
    ensure_file_exist()
    load_data()
    main_menu()

main()