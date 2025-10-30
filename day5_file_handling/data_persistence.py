#TASK3: Data Persistence – Student Manager v2
import json

students = {
    "S101": {"name": "John", "age": 18, "clubs": ["Robotics", "Sports"]},
    "S102": {"name": "Maya", "age": 19, "clubs": ["Music"]}
}
with open("students.json", "w") as file:
    json.dump(students, file, indent=4)


with open("students.json", "r") as file:
    data = json.load(file)

for student_id, info in data.items():
    print(f"\nId: ", student_id)
    print("name: ", info["name"])
    print("age: ", info["age"])
    print("clubs: ",", ".join(info["clubs"]))

'''What advantage does JSON have over plain text?'''
# JSON allows you to store structured data such as lists and dictionaries
'''Why is json.dump() + json.load() safer than eval()?'''
# It is because eval() interprets any string inputed as executable code
# this can result in malicious viruses and cyber-attacks.
# On the other hand, json..() doesnt execute anything, and merely stores data.