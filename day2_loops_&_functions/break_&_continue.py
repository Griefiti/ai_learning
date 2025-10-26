for i in range(1,10):
    if i == 7:
        print(f"We found {i}, exit the premises immediately")
        break         # exits the loop immediately
    print(i)

for i in range(1,4):
    if i == 2:
        print(f"{i} got skipped.")
        continue      # skips the current iteration and directly moves onto the next in the loop    
    print(i)

#TASK 3A - Input Break
while True:
    user = input("What is your favourite word: ")
    if user == "exit":
        print("Thanks for playing!")
        break
    else:
        print(f"Me too!,{user} is also my favourite word.")
        print("If u would like to leave the program, type 'exit' as your favourite word.")

#TASK 3B - Divisible by 3
for i in range(1,11):
    if i % 3 == 0:
        continue
    print(i)

'''What's the difference between break and continue in your own words?'''
# I imagine, break as a sniper with only one target in mind. If they find you, BREAK! EXIT THAT LOOP!, while continue is one or more targets. Ok, they found one, next in line please! We don't got all day. I imagine continue as a prison guard sorting between prisoners. Which ones should go to the normal prison and which to maximum security.
'''When would you prefer a while True + break setup over a normal while loop?'''
# I would rather use while True + break setup when its more complex or when there are multiple conditions to BREAK. I would use a normal while loop for more elementary conditions, i know exactly when and why the while loop will exit.

#BONUS---------------------------------------------------------
for i in range(2,101):
    for j in range(2,8):      
        if i != j:              
            if i % j == 0: 
                break
    else:
        print(i)
                
# prime number generator from 2 - 100, since 1 aint no prime
# I just chose up to 7 since most or all numbers higher are divisible by these 6 digits (2-7).8 by 2, 9 by 3, 10 by 2 & 5 
# Therefore, if i have all the rudimentary numbers, they could divide all the higher numbers.
# This is purely intuition, i didnt check if its actually correct above 100 digits.
# i didnt know u dont need to align the else with the if statements, took me much longer to make then expected.
