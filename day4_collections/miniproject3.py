# ============================================================
#  Project: Student Data & Club Manager
#  Author: [Sai Thant Zin]
#  Date: [30/10/2025]
#
#  Description:
#  A menu-driven Python program to manage student data using
#  tuples, sets, and dictionaries. Each student record contains:
#     - Tuple (Name, Age, Club Set)
#     - Set ensures each student’s clubs are unique
#     - Dictionary stores all students using their ID as key
#
#  Features:
#     1. Add a new student
#     2. View all students
#     3. Add club(s) to a student (case-insensitive)
#     4. Remove club(s) from a student (case-insensitive)
#     5. Search students by club
#     6. Exit the program
#
#  Notes:
#  - The sample dataset below is provided for quick testing/demo.
#  - You may set USE_SAMPLE_DATA = False to start with an empty dataset.
# ============================================================

# ===== SAMPLE DATA =====
USE_SAMPLE_DATA = True
if USE_SAMPLE_DATA:
    students = {
    "S101": ("Aiden", 18, {"Coding", "Music", "Robotics"}),
    "S102": ("Ben", 19, {"Drama", "Sports"}),
    "S103": ("Chloe", 20, {"Art", "Coding", "Music"}),
    "S104": ("Derek", 18, {"Photography", "Nature"}),
    "S105": ("Faith", 19, {"Music", "Sports"}),
    "S106": ("Ethan", 21, {"Drama", "Chess"}),
    "S107": ("Grace", 20, {"Coding", "Music", "Sports"}),
    "S108": ("Hannah", 18, {"Art", "Dance"})
    }
else:
    students = {}

options = ("Add Student", "View All Students", "Add Club", "Remove Club", "Search by Club", "Exit")

def add_student():
    clubs = set()
    while True:
        while True:
            input_id = input("Please enter the Student ID number: ")                                                      
            if input_id.lower() in [id.lower() for id in students]:
                print("Student ID number already in the list.") 
                continue
            else:
                break

        name = input("Please enter the Student's name: ")

        while True: 
            age = input("Please enter the Student's age: ")
            if not age.isdigit() or not(1 <= int(age) <= 100):
                print("Please enter in a valid age.")
            else:
                break
        while True:
            club = input("Please enter the club(s) the student is in: ")
            if club.lower() in [c.lower() for c in clubs]:
                print("Club already in the list.") 
            clubs.add(club)
            again = input("Would you like to add another club?(yes/no) ")
            if again == "no":
                break

        students[input_id] = (name, age, clubs)

        add_again = input("Would you like to add again?(yes/no) ")
        if add_again == "no":
            break
def list_student():
    i = 1
    if students != {}:
        print(f"{'List':-<40}")
        for id, student in students.items():
            name, age, clubs = student
            print(f"\n{i})")
            print("ID   : ", id)
            print("Name : ", name) 
            print("Age  : ", age)
            print("Clubs: ", clubs)
            i += 1

        print(f"You have {i - 1} students in the list.")
    else:
        print("You haven't added anything to the list!")    
def add_club():
    while True:
        list_student()
        if students == {}:
            break
        while True:
            id_input = input("Please select a student by entering their student ID number: ")
            if id_input in students:

                while True:
                    club = input("Please enter the club(s) to add: ")
                    if club.lower() in [c.lower() for c in students[id_input][2]]:
                        print("Club already in the list.")
                        continue 
                    students[id_input][2].add(club) # improved
                    again = input("Would you like to add another club?(yes/no) ")
                    if again == "no":
                        break

                    '''   
                    for id,(_, _, clubs)  in students.items(): # Old but I like how the unpacking looks
                        if id == id_input:
                            clubs.add(club)
                    '''    
            else: 
                print("Invalid Student Id!")
                continue

            break
            
        add_again = input("Would you like to add again?(yes/no) ")
        if add_again == "no":
            break      
def remove_club():
    while True:
        list_student()
        if students == {}:
            break
        while True:
            id_input = input("Please select a student by entering their student ID number: ")
            if id_input in students:

                while True:
                    found = None
                    club = input("Please enter the club(s) to remove: ")
                    for c in students[id_input][2]:
                        if club.lower() == c.lower():
                            club = c
                            found = "yes"
                            break

                    if found == "yes":
                        students[id_input][2].remove(club)
                    else:
                        print("Club not found! Try again.")
                        continue

                    again = input("Would you like to remove another club?(yes/no) ")
                    if again == "no":
                        break

            else: 
                print("Invalid Student Id!")
                continue

            break

        remove_again = input("Would you like to remove again?(yes/no) ")
        if remove_again == "no":
            break
def search_club():
    found = False
    i = 1
    search = input("Please enter club name: ")

    print(f"{search} Club Members:")

    for _,(name,_,clubs) in students.items():
        for c in clubs:
            if search.lower() == c.lower():
                print(f"{i}) {name}")
                found = True
                i += 1

    if not found:
        print("\nNone found.")
def exit():
    print("Exiting program.. Have a Nice Day!")
def logic(ans):
    match ans:
        case "1":
            add_student()
        case "2":
            list_student()
        case "3":
            add_club()
        case "4":
            remove_club()
        case "5":
            search_club()
        case "6":
            exit()
        case _:
            print("Please only type a number from 1 to 6!")
def main_menu():
    while True:
        print(f"\n{'<Main Menu>':=^27}")
        for i in range(len(options)):
            print(f"{'Option ' + str(i+1) + ':':<10}{options[i]}")
        answer = input("Please select an option(1-6): ")
        print()
        logic(answer)
        if answer == "6":
            break

main_menu()
