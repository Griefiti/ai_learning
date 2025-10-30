#TASK1: File Writing & Reading Basics
entries = []
for i in range(1,4):
    entries.append(input(f"Please enter your entry {i}:\n"))

with open("journal.txt", "w") as file:
    file.write(f"{' My Journal ':=^16}\n")
    for i in range(3):
        file.write(f"{i+1}) {entries[i]}\n")

with open("journal.txt", "r") as file:
    print(file.read())

with open("journal.txt", "a") as file:
    file.write("\n<Outro>\n")
    file.write("I hope yall have a good day!")

'''What happens if you open the file in 'w' mode multiple times?'''
# Mode 'w' stands for write/overwrite, which implies that.. 
# ..if a file with the same name already exists, it will override instead of creating new files.
'''How does 'a' mode behave differently?'''
# Mode 'a' stands for append, which means..
# ..it will add to the end of the file, just like how i added an outro.
'''Why is the with open() method preferred over manually closing files?'''
# Because with open() automatically closes the files.
# There is no longer a need to call file.close()
# Reduces Human error / forgetting to close.

#BONUS---------------------------------------------------------------------
with open("smiley_face.txt", "w") as file:
    file.write("-----------")
    file.write(f"\n|  -   -  |")
    file.write(f"\n|    |    |")
    file.write(f"\n| \_____/ |")
    file.write(f"\n \\       /")
    file.write("\n" + "  -------")

with open("smiley_face.txt", "r") as file:
    content = file.read()
    print(content)

# I made a smiley face, but had some trouble wiht backslashes