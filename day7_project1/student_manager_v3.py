import csv
import os
students = []

# ----BASE PATH SETUP----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

file = "students.csv"
FILE_PATH = os.path.join(DATA_DIR, file)

#==================================
# FILE HANDLING
#==================================
def ensure_files_exist():
    try:
        if not os.path.exists(FILE_PATH):
            with open(FILE_PATH, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["id","name","age","subjects","clubs"])
            print(f"Created missing file: {file}")
    except Exception as e:
        print(f"Unable to verify or create {file} due to ({e}).")
        return


def load_data():
    global students
    with open(FILE_PATH, "r") as f:
        reader = csv.DictReader(f)
        students = list(reader)
        for r in students:
            for key in ["subjects", "clubs"]:
                r[key] = r[key].replace(";",", ")
                r[key] = r[key].replace(";",", ")


def save_data():
    global students
    for r in students:
        for key in ["subjects", "clubs"]:
            r[key] = r[key].replace(", ",";")
            r[key] = r[key].replace(", ",";")

    with open(FILE_PATH, "w", newline="") as f:
        fieldnames = ["id","name","age","subjects","clubs"]
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        writer.writerows(students)
    
    print("Data Saved successfully!")

#==================================
# MODIFICATIONS
#==================================

def modify_student():
    while True:
        print("\n====== LIST MODIFICATION ======")
        print("Option 1: Add Student")
        print("Option 2: Remove Student")
        print("Option 3: Update Student")
        print("Option 4: Return to Main Menu")
        choice = input("Select an option(1-4): ").strip()

        if not choice or not choice.isdigit():
            print("\nInvalid option. Try again!"); continue
        if not (1 <= int(choice) <= 4):
            print("\nPlease enter a number from (1-4)"); continue
        
        if   choice == "1": add_student()
        elif choice == "2": remove_student()
        elif choice == "3": update_student()
        elif choice == "4": print("\nReturning to Main Menu.."); break

#-----------------------------
# Helper Functions
#-----------------------------
def input_name():
    while True:
        name = input("Name: ").strip()
        if not name: 
            print("Invalid input. Try again."); continue
        
        split_name = name.split(" ")
        cap_name = [n.capitalize() for n in split_name]
        name = " ".join(cap_name); break
    
    return name

def input_age():
    while True:
        age = input("Age: ").strip()
        if not age or not age.isdigit():
            print("Invalid input. Try again."); continue
        if not (0 < int(age) < 100):
            print("Age must be a positive number."); continue
        break

    return age

def input_subjects():
    subjects = []
    while True:
        subject = input("Subjects: ").strip().capitalize()
        if not subject: 
            print("Invalid input. Try again.\n"); continue
        
        subjects.append(subject)
        
        again = input("\nWould you like to add another subject?(yes/no) ")
        if again == "yes": continue
        else: subjects = ", ".join(subjects); break

    return subjects

def input_clubs():
    clubs = []
    while True:
        club = input("Clubs: ").strip().capitalize()
        if not club: 
            print("Invalid input. Try again.\n"); continue
        
        clubs.append(club)
        
        again = input("\nWould you like to add another club?(yes/no) ")
        if again == "yes": continue
        else: clubs = ", ".join(clubs); break
        
    return clubs
#-----------------------------

def add_student():
    global students
    while True:
        print("\n== Student to Add ==")
        #---------------------------------------------------------------------    
        while True:
            student_id = input("ID: ").strip().capitalize()
            if not student_id: 
                print("Invalid input. Try again."); continue
            if student_id in [i["id"] for i in students]:
                print("The student id is already in the list!"); continue
            if student_id.startswith("S") and student_id[1:].isdigit():
                if len(student_id[1:]) == 3 and (1 <= int(student_id[1:]) <= 999): break

            print("Student IDs can only be in the format of S(001-999).")
            print("For example: S001, S212, S800, S437"); continue
        #---------------------------------------------------------------------
        name = input_name()
        age = input_age()
        subjects = input_subjects()
        clubs = input_clubs()
        #---------------------------------------------------------------------    
        '''CONFIRMATION'''
        print("\n== Confirm Student to Add ==")
        print(f"\n{'ID:':<9}",    student_id)
        print(f"{'Name:':<9}",    name)
        print(f"{'Age:':<9}",     age)
        print(f"{'Subjects:':<9}",subjects)
        print(f"{'Clubs:':<9}",   clubs)

        confirm = input("\nPlease type 'confirm' for confirmation: ")
        if confirm != "confirm": continue

        students.append({
            "id"      : student_id,
            "name"    : name,
            "age"     : age,
            "subjects": subjects,
            "clubs"   : clubs
        })

        break
    

def remove_student():
    global students
    while True:
        list_student()

        print("\n== Student to Remove ==")
        id_input = input("Enter an ID: ").strip()
        if id_input not in [r["id"] for r in students]:
            print("Invalid ID! Try again."); continue

        for i, r in enumerate(students):
            if id_input == r["id"]:
                pos = i
                '''CONFIRMATION'''
                print("\n== Confirm Student to Remove ==")
                print(f"\n{'ID:':<9}",    r["id"])
                print(f"{'Name:':<9}",    r["name"])
                print(f"{'Age:':<9}",     r["age"])
                print(f"{'Subjects:':<9}",r["subjects"])
                print(f"{'Clubs:':<9}",   r["clubs"])

                confirm = input("\nPlease type 'confirm' for confirmation: ")
                if confirm != "confirm": break  

                print(f"Successfully removed student ({students[pos]["id"]}).")
                del students[pos]
            
                return
        

def update_student():
    global students
    while True:
        list_student()

        print("\n== Student to Update ==")
        id_input = input("Enter an ID: ").strip()
        if id_input not in [r["id"] for r in students]:
            print("Invalid ID! Try again."); continue

        for r in [r for r in students if id_input == r["id"]]:
            print(f"\n{'ID:':<9}",    r["id"])
            print(f"{'Name:':<9}",    r["name"])
            print(f"{'Age:':<9}",     r["age"]) 
            print(f"{'Subjects:':<9}",r["subjects"])
            print(f"{'Clubs:':<9}",   r["clubs"])
        break

    while True:
        print("\n=== Update Menu ===")
        print("Option 1: Name")
        print("Option 2: Age")
        print("Option 3: Subjects")
        print("Option 4: Clubs")
        choice = input("Select an option(1-4): ").strip()
        print()

        if not choice or not choice.isdigit():
            print("Invalid option. Try again!"); continue
        if not (1 <= int(choice) <= 4):
            print("Please enter a number from (1-4)"); continue
        
        for i, r in enumerate(students):
            if id_input == r["id"]:
                #================================================================
                if   choice == "1": 
                    update = input_name()

                    print("Current Name: ", students[i]["name"])
                    print("Updated Name: ", update)

                    confirm = input("\nPlease type 'confirm' for confirmation: ")
                    if confirm != "confirm": continue

                    students[i]["name"]     = update
                    return
                #================================================================
                elif choice == "2":
                    update = input_age() 

                    print("Current Age: ", students[i]["age"])
                    print("Updated Age: ", update)

                    confirm = input("\nPlease type 'confirm' for confirmation: ")
                    if confirm != "confirm": continue

                    students[i]["age"]      = update 
                    return  
                #================================================================
                elif choice == "3": 
                    update = input_subjects()

                    print("Current Subjects: ", students[i]["subjects"])
                    print("Updated Subjects: ", update)

                    confirm = input("\nPlease type 'confirm' for confirmation: ")
                    if confirm != "confirm": continue

                    students[i]["subjects"] = update
                    return
                #================================================================
                elif choice == "4": 
                    update = input_clubs()

                    print("Current Clubs: ", students[i]["clubs"])
                    print("Updated Clubs: ", update)

                    confirm = input("\nPlease type 'confirm' for confirmation: ")
                    if confirm != "confirm": continue

                    students[i]["clubs"]    = update 
                    return
                #================================================================       

#==================================
# DISPLAY
#==================================

def view_student():
    while True:
        print("\n======== LIST VIEWING ========")
        print("Option 1: Search Student")
        print("Option 2: List Student")
        print("Option 3: Sort Student")
        print("Option 4: Return to Main Menu")
        choice = input("Select an option(1-4): ").strip()
        print()

        if not choice or not choice.isdigit():
            print("Invalid option. Try again!"); continue
        if not (1 <= int(choice) <= 4):
            print("Please enter a number from (1-4)"); continue
        
        if   choice == "1": search_student()
        elif choice == "2": list_student()
        elif choice == "3": sort_student()
        elif choice == "4": print("Returning to Main Menu.."); break


def search_student():
    global students
    if not students:
        print("The list is empty."); return
    
    while True:
        list_student()

        print("\n== Search Engine ==")
        id_input = input("Enter an ID: ").strip()
        if id_input not in [r["id"] for r in students]:
            print("Invalid ID! Try again."); continue
        break
        
    for r in [r for r in students if id_input == r["id"]]:
        print(f"\n{' SEARCHED STUDENT ':=^35}")
        print(f"{'\n<ID ' + r["id"] + ">":^35}")
        print(f"{'Name:':<9}",    r["name"])
        print(f"{'Age:':<9}",     r["age"]) 
        print(f"{'Subjects:':<9}",r["subjects"])
        print(f"{'Clubs:':<9}",   r["clubs"])

        return
        

def list_student():
    global students
    if not students:
        print("The list is empty."); return
    
    count = len(students)
    print(f"{' STUDENT LIST ':=^35}")

    for r in students:
        print(f"\n{'<ID ' + r["id"] + ">":^35}")
        print(f"{'Name:':<9}",    r["name"])
        print(f"{'Age:':<9}",     r["age"])
        print(f"{'Subjects:':<9}",r["subjects"])
        print(f"{'Clubs:':<9}",   r["clubs"])
        
    print(f"\nStudent Count: {count}")
    print(f"\n{' END OF LIST ':=^35}")

    return


def sort_student():
    global students
    if not students:
        print("The list is empty."); return
    
    print("Sorting list from S001 to S999...")

    sorted_list = []
    id_list = [int(r["id"][1:]) for r in students]
    i = 0
    n = len(id_list)
    while i < n:
        j = i
        min_index = j
        while j < n-1:
            if id_list[min_index] > id_list[j+1]:
                min_index = j+1
            j += 1
        id_list[i], id_list[min_index] = id_list[min_index], id_list[i]
        i += 1

    for i in id_list:
        for r in students:
            if int(r["id"][-3:]) == i:
                sorted_list.append(r)
    students = sorted_list
    
    print(f"\n{' (SORTED VERSION) ':=^35}")
    list_student()    

#==================================
# MAIN ENTRY POINT
#==================================

def main_menu():
    while True:
        print("\n===== STUDENT MANAGER =====")
        print("Option 1: View Student List")
        print("Option 2: Modify Student List")
        print("Option 3: Exit")
        choice = input("Select an option(1-3): ").strip()

        if not choice or not choice.isdigit():
            print("\nInvalid option. Try again!"); continue
        if not (1 <= int(choice) <= 3):
            print("\nPlease enter a number from (1-3)"); continue
        
        if   choice == "1": view_student()
        elif choice == "2": modify_student()
        elif choice == "3": print("\nExitting program.."); break
            
def main():
    ensure_files_exist()
    load_data()
    main_menu()
    save_data()

main()