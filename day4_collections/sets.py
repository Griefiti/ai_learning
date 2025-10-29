#TASK2 - Friend List Manager
school_friends = {"Patrick", "Tommy", "Michael", "Jimmy", "Prince", "Ryan", "Harrison", "Steve", "Ethan", "Steven", "Stephen"}
discord_friends = {"Aaron", "Steve", "William", "Peter", "Liam", "Zanny", "Ken", "Patrick", "Kuki", "Tommy", "Michael", "Dexter", "Steven"}

print("Entire List of friends:", school_friends | discord_friends)
print("Friends at school only:", school_friends - discord_friends)
print("Friends from both worlds:", school_friends & discord_friends)

discord_friends.add("Ryan")
discord_friends.remove("Dexter")
school_friends.add("Phillip")

'''Sets are best used when _____.'''
# you just need to check for duplicates and there is no need for indexing and order.
'''They helped me realize that duplicates are _____.'''
# easily identifiable and removable using sets? Sets automatically remove duplicates.

#BONUS---------------------------------------------------------------------------------------------------------------
#Lottery TOTO
winning_numbers = {'3','38','21','14','7','11'}
def number_input():
    your_numbers = set()
    i = 0
    while i < 6:
        num = input("What numbers would you like to pick?(1-49) ")
        if not num.isdigit() or not (1 <= int(num) <= 49):
            print("Invalid number (1-49)")
            continue
        if num in {numbers for numbers in your_numbers}:
            print("you've already entered this number.")
            continue

        your_numbers.add(num)
        i += 1
    return your_numbers
def matching(same):
    match same:
        case 1 | 2 :
            print("Sadly, you won nothing!")
        case 3:
            print("You won $50!")
        case 4:
            print("You won $1000!")
        case 5:
            print("You won $100k!")
        case 6:
            print("Congratulations! You won the grand prize of $10 Million dollars!")
        case _:
            print("No matches, better luck next time.")

print("WELCOME to the TOTO LOTTERY!")

your_numbers = number_input()
common = len(your_numbers & winning_numbers)

print("The winning numbers this week are:", winning_numbers)
print("Your numbers are:", your_numbers)
print(f"You have {common} matching numbers.")
matching(common)

# Since sets are unordered, your numbers can be typed in any order. 
# Afterwards, just check the intersecting/same numbers in the sets.
