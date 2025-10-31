import csv

with open("students_list.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)
    #TASK2A: Average Age
    for row in data:
        row["age"] = int(row["age"])

    age = [(row["age"]) for row in data]
    avg_age = sum(age)/len(age)

    print("Average age: {:.2f}".format(avg_age))

    #TASK2B: Youngest and Oldest Student
    max_age = max(age)
    min_age = min(age)

    for row in data:
        if min_age == (row["age"]):
            youngest_name = row["name"] # Whats a faster way?
    for row in data:
        if max_age == (row["age"]):  # I'm at a point where formatting and shortcuts matter a lot..
            oldest_name = row["name"]   # ..Also cleaner and more practical code.

    #youngest_name = [row["name"] for row in data if min_age == int(row["age"])]
    #oldest_name = [row["name"] for row in data if max_age == int(row["age"])]

    print(f"{youngest_name} is the youngest student in the class. He is {min_age} years old.")
    print(f"{oldest_name} is the oldest student in the class. He is {max_age} years old.")

    #TASK2C: Only Grade A students
    gradeA_names = [row["name"] for row in data if row["grade"] == "A"]
    print("Students with Grade A:")
    for i, name in enumerate(gradeA_names, 1):
        print(f"{i}.", name)
    
    #TASK2D: Saving List
    with open("grade_a.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Students with Grade A:"])
        for name in gradeA_names:
            writer.writerow([name])
