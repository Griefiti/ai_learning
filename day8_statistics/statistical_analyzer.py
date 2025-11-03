import csv, math, os
data = []
temp = []
# === BASE PATH SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

#------FILE HANDLING------
def ensure_files_exist(FILE_PATH, file):
    try:
        if not os.path.exists(FILE_PATH):
            print(f"Missing file: {file}")
            return False
    except Exception as e:
        print(f"Unable to verify {file} due to ({e}).")
        return False
    
    return True


def load_data(FILE_PATH):
    global data
    global temp
    with open(FILE_PATH, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                row["Score"] = float(row["Score"])
                temp.append(row["Score"])
                data.append(row)
            except ValueError:
                continue

        print(data)

def save_data(file):
    global DATA_DIR
    pos = file.find(".")
    name = file[:pos]
    file_name = name + "_summary.csv"
    new_file_path = os.path.join(DATA_DIR, file_name)
    summary = [{
        "Mean"  :mean(),
        "Median":median(),
        "Mode"  :mode(),
        "Range" :value_range(),
        "Stdev" :standard_deviation()
    }]
    with open(new_file_path, "w", newline="") as f:

        fieldnames = ['Mean','Median','Mode','Range','Stdev']
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(summary)
    
    print("Data Saved successfully!")
#=========================
# CALCULATIONS
#=========================
def mean():
    global temp
    total = 0
    num = len(temp)
    for n in temp:
        total += n
    return round(total / num, 2)


def median():
    global temp
    sorted_list = sorted(temp)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return (sorted_list[int(mid)])


def mode():
    global temp
    counts = {}
    for num in temp:
        counts[num] = counts.get(num, 0) + 1
    return max(counts, key = counts.get)
        

def value_range():
    global temp
    return max(temp) - min(temp)


def standard_deviation():
    global temp
    avg = mean()
    variance = sum((num - avg) ** 2 for num in temp) / len(temp)
    return round(math.sqrt(variance),2)


#==================================
# MAIN ENTRY POINT
#==================================

def calculations():
    print("\n===== Statistical Analyzer =====")

    print(f"\nMean   : {mean():>6}")
    print(f"Median : {median():>6}")
    print(f"Mode   : {mode():>6}")
    print(f"Range  : {value_range():>6}")
    print(f"Stdev  : {standard_deviation():>6}")

def main():
    while True:
        file = input("Please enter file name: ").strip()
        FILE_PATH = os.path.join(DATA_DIR, file)
        if not ensure_files_exist(FILE_PATH, file):
            continue
        load_data(FILE_PATH)
        calculations()
        choice = input("\nWould you like to save(yes/no) ")
        if choice == "yes":
            save_data(file)
        break

main()