import csv

students = [
    ["id", "name", "age", "grade"],
    [1, "Alex", 17, "A"],
    [2, "Jamie", 18, "B"],
    [3, "Tyler", 17, "B"],
    [4, "Samuel", 19, "A"],
    [5, "Chris", 16, "C"],
]
#TASK1A: creating a csv file
with open("students_list.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerows(students)

#TASK1B: appending the csv file
with open("students_list.csv", "a", newline = "") as f:
    new_student = [6, "Michael", 18, "B"]
    
    writer = csv.writer(f)
    writer.writerow(new_student)

#TASK1C: formatting and reading from the csv file
with open("students_list.csv", "r") as f: 
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("students_list.csv", "r") as f: 
    reader = csv.DictReader(f)
    name_input = input("Please enter a student name: ")
    for row in reader:
        if name_input.lower() == row["name"].lower():
            print("Searched Name:",row["name"])
            print("ID:",row["id"])
            print("Age:",row["age"])
            print("Grade:",row["grade"])
    else:
        print("No name Found!")

'''How tabular data can be stored and read back'''
# Tabular data can be stored in csv files and be read using the csv module. 
# From which, you use csv.reader and csv.DictReader to extract the information.
'''How csv.reader vs csv.DictReader differ'''
# csv.reader converts the tabular data into lists, and csv.DictReader converts the data into dictionaries.
'''How to build reusable CSV utilities for data analysis'''
# You can create a file containing basic csv to python converters and python to csv. 
# Add user inputs for different files, and maybe options to choose the type of analysis or formatting the user needs.

#BONUS----------------------------------------------------------------------------------
# Turning dictionaries into csv

students2 = [
{'ID': '1', 'Name': 'Alice Tan', 'Age': '18', 'Club': 'Robotics', 'Member': 'True', 'Subjects': 'Math, Physics'},
{'ID': '2', 'Name': 'Bob Lim', 'Age': '19', 'Club': 'Music', 'Member': 'False', 'Subjects': 'English, History'},
{'ID': '3', 'Name': 'Charlie Ong', 'Age': '18', 'Club': 'Drama', 'Member': 'True', 'Subjects': 'Art, Literature'},
{'ID': '4', 'Name': 'Dana Lee', 'Age': '20', 'Club': 'Sports', 'Member': 'True', 'Subjects': 'PE, Biology'},
{'ID': '5', 'Name': 'Evan Chua', 'Age': '19', 'Club': 'Chess', 'Member': 'False', 'Subjects': 'Math, Computer Science'},
{'ID': '6', 'Name': 'Fiona Goh', 'Age': '18', 'Club': 'Music', 'Member': 'True', 'Subjects': 'Music, History'},
{'ID': '7', 'Name': 'Gabriel Tan', 'Age': '21', 'Club': 'Robotics', 'Member': 'True', 'Subjects': 'Physics, Engineering'},
{'ID': '8', 'Name': 'Hannah Wong', 'Age': '19', 'Club': 'Drama', 'Member': 'False', 'Subjects': 'Literature, Art'},
{'ID': '9', 'Name': 'Ian Koh', 'Age': '18', 'Club': 'Sports', 'Member': 'True', 'Subjects': 'PE, Health'},
{'ID': '10', 'Name': 'Jasmine Low', 'Age': '20', 'Club': 'Chess', 'Member': 'True', 'Subjects': 'Math, Statistics'},
{'ID': '11', 'Name': 'Kenny Ng', 'Age': '22', 'Club': 'Music', 'Member': 'True', 'Subjects': 'Music, Philosophy'},
{'ID': '12', 'Name': 'Lydia Chan', 'Age': '17', 'Club': 'Robotics', 'Member': 'False', 'Subjects': 'Science, Technology'},
{'ID': '13', 'Name': 'Marcus Lim', 'Age': '19', 'Club': 'Drama', 'Member': 'True', 'Subjects': 'Art, Theatre'},
{'ID': '14', 'Name': 'Natasha Goh', 'Age': '20', 'Club': 'Music', 'Member': 'True', 'Subjects': 'Music, English'},
{'ID': '15', 'Name': 'Oscar Teo', 'Age': '18', 'Club': 'Chess', 'Member': 'False', 'Subjects': 'Math, Economics'},
{'ID': '16', 'Name': 'Priya Singh', 'Age': '21', 'Club': 'Robotics', 'Member': 'True', 'Subjects': 'Engineering, AI'},
{'ID': '17', 'Name': 'Quincy Lau', 'Age': '19', 'Club': 'Drama', 'Member': 'False', 'Subjects': 'Literature, Design'},
{'ID': '18', 'Name': 'Rachel Tan', 'Age': '20', 'Club': 'Sports', 'Member': 'True', 'Subjects': 'Biology, Chemistry'},
{'ID': '19', 'Name': 'Samuel Ng', 'Age': '19', 'Club': 'Robotics', 'Member': 'True', 'Subjects': 'Technology, Math'},
{'ID': '20', 'Name': 'Tiffany Lee', 'Age': '22', 'Club': 'Music', 'Member': 'False', 'Subjects': 'English, Music Theory'},
{'ID': '21', 'Name': 'Umar Aziz', 'Age': '18', 'Club': 'Drama', 'Member': 'True', 'Subjects': 'Theatre, Art'},
{'ID': '22', 'Name': 'Valerie Ong', 'Age': '19', 'Club': 'Chess', 'Member': 'True', 'Subjects': 'Computer Science, Math'},
{'ID': '23', 'Name': 'Wilson Tan', 'Age': '20', 'Club': 'Sports', 'Member': 'False', 'Subjects': 'PE, Physics'},
{'ID': '24', 'Name': 'Xavier Chua', 'Age': '21', 'Club': 'Robotics', 'Member': 'True', 'Subjects': 'AI, Engineering'},
{'ID': '25', 'Name': 'Yasmin Ho', 'Age': '18', 'Club': 'Music', 'Member': 'True', 'Subjects': 'Music, History'}
]

with open("students_dict.csv", "w", newline = "") as f:
    fieldnames = ["ID", "Name", "Age", "Club", "Member", "Subjects"]

    writer = csv.DictWriter(f, fieldnames)
    writer.writeheader()
    writer.writerows(students2)

with open("students_dict.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#NICE, i can convert dictionaries into lists and vice versa.
