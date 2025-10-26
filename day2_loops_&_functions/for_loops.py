for i in range(3):
    print("I am Groot!")

for i in range(1,9): # range(start, stop, step)
    print(i, i * 2)  # range(stop is exclusive)

for i in range(1,10,3):
    print(f"Number {i}")

#TASK1 - for loops
for i in range(1,11):
    print(f"{i} squared is {i ** 2}")

'''what does i represent, and how does range(1, 11) decide when to stop?'''
# i is a incremental or decremental variable used in a loop based of a sequence, list, array which determines how long the loop is. In all fairness, i is just a variable name. You could replace it with literally anything else.
# You look at the second number, which corresponds to range(stop). However the stop is exclusive, therefore 11 - 1 = 10. The actual loop will stop at number 10.

#BONUS
a = 2
b = 3
print(a)
print(b)
for count in range(1,8):
    c = a * b
    a = b
    b = c 
    print(f"{count}: ", c)
# This for loop displays a multiplication version of the fibonnacci sequence. 
# I tried making the exponential version before this, but too many numbers valueError.