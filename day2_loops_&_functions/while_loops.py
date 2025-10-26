count = 1
while count <= 3:
    print(count, "Konnichiwa!")
    count += 1

#TASK2A - n sequence
n = 1
while n <= 10:
    print(f"Current number: {n}")
    n += 1   # Always remember to update the variable

#TASK2B - countdown timer
counter = 10
print("<Liftoff in>")
while counter > 0:
    print(counter)
    counter -= 1
print("BOOM!!!")
print("Houston, we have liftoff!")

'''1. How is a while loop different from a for loop?''' 
# A while loop uses conditional logic to maybe run forever. On the other hand, a for loop uses sequences, lists, etc.. to run for a set number of times.
'''2. What happens if you forget to update the variable in a while loop?'''
# You would be stuck in an infinite loop and might crash your computer.

#BONUS
answer = ""
while answer.lower() != "yes":
    answer = input("Will you marry me? ")
    if answer == "no":
        print("Please try again. or You'll be stuck in this time loop with me FOREVER!")
    elif answer != "yes":
        print("Please give me a proper answer.")
print("Do you want to go get some shawarma? My treat")
# BTW i just noticed, does while loops require a variable outside the loop to start with?
# I remember u dont need it for do while loops and while True: