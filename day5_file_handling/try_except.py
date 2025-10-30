#Task2: Line-by-Line Reading & File Validation
user_input = input("Please enter a file name + file type: ")

try:
    with open(user_input, "r") as file:
        i = 1 
        print(f"{'File-Contents':=^20}\n")
        for line in file:
            print(f"Line {i:>2})",line.strip())
            i += 1

except FileNotFoundError:   
    print("File not found! Exitting program")

'''What error type did we catch?'''
# We caught a FileNotFoundError.
# As the name suggests, it occurs when the file is not found.
'''Why is it better than letting the program crash?'''
# When the program crashes, thats the end. You cant fix anything.
# Now you have other options that the program can do, when an error occurs. 
'''How does reading line by line help for very large files?'''
# I haven't tested it but it will probably be much much faster than reading everything first..
# ..then printing it all at once.

#BONUS-------------------------------------------------------------------------------
with open(user_input, "r") as file:

    total_words = 0
    total_letters = 0

    lines = file.readlines()

    for line in lines:
        total_words += len(line.split())
        total_letters += len(line.replace(" ","").replace("\n",""))

    print("<Word Count>")
    print(f"{user_input} has {total_words} words and {total_letters} letters.")

# I made a Word and Letter Counter
    



