#TASK3 = numbers
num1 = int(input("Type your number 1: "))
num2 = float(input("Type your number 2: "))

print("Addition: ", num1 + num2)
print("Subtraction: ", num1 - num2)
print("Multiplication: ", num1 * num2)
print("Division: ", num1 / num2)
# seems like you can mesh float and int

"What's the difference between int() and float()?"
# when you input a decimal number in int(),
# you get a ValueError, because int() only accepts whole numbers
# float() for decimal numbers
"Why does input() always return a string, even when you type numbers?"
# I guess input() always return a string because it is the most common type a user can input.
# If it was something else, having to specify which, would just be inefficient.
# String kind of like a universal data type.

#BONUS
num3 = int(input("What number do you want for your multiplication table: "))
print("Multiplcation table")
for i in range(10):
    print(num3 *(i+1))