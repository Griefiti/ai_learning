#TASK1 - Tuple Basics
person = ("Allison", 34, "New York", "Nurse")
name, age, city, occupation = person
print(f"Her name is {name}, and she is {age} years old.")
print(f"Currently working as a {occupation} in {city}.")

# person[0] = "James" 
# you get a TypeError because tuples are immutable

'''when would immutability be useful?'''
# When you have something constant you dont want changed. 
# you can have a reference tuple, a tuple that stores passwords, or someone's personal info and id.

#BONUS-------------------------------------------------------
UserId = ("gangasta4", "5tarry_day", "0ceanist", "picture_punk3")
Passcode = ("1234", "0000", "1212", "5656")
count = 0

def login():
    global count
    index = int(input("Which account would you like to open?(1-4): "))
    while True:
        username = input(f"\nPlease enter UserId for account {index}: ")
        password = input(f"Please enter passcode for account {index}:")

        if username == UserId[index - 1] or password == Passcode[index - 1]:
            print("Logging in shortly:")
            print("Please wait a moment")
            break
        else:
            print("\nWrong UserId and Passcode.")
            if count < 3:
                if count != 2:
                    print(f"You have {3 - count} attempts remaining.")
                else:
                    print(f"You have {3 - count} attempt remaining.")
                count += 1
            else:
                print("Too many attempts! For the safety of your account, we will be locking it for the 24 hours.")
                print("As we have stated when you first open your account. If you have truly forgetten your userId or Passcode, please create a new account.")
                break
login()
# I made a login page where your userid and password are permanent. 
