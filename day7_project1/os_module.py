import os

# === BASE PATH SETUP ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "test_files")
os.makedirs(DATA_DIR, exist_ok=True)

file = "test.csv"
FILE_PATH = os.path.join(DATA_DIR, file)

try:
    if not os.path.exists(FILE_PATH):
        open(FILE_PATH, "a").close()  # open files in "a" mode to avoid data loss.
        print(f"Created missing files: {file}")
except Exception as e:
    print(f"Could not verify or create {file} due to ({e})")