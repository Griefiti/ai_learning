#TASK4 - Conditional Logic
score = int(input("What did you get on your exam today(1-100): "))
if score > 100 or score < 0:
    print("Invalid score.")
elif score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else: 
    print("You failed your exam!")

"why do we use elif instead of multiple ifs?"
# We use elif instead of multiple if because, the elif should only run when the first condition fail.
# If you use multiple ifs instead, your value can sometimes fill multiple conditions.
"What happens when two conditions overlap?"
# When two conditions overlap, the one that comes first will work first. 
# If its is one if and one elif, only the if will work. If it is two if conditions, both will work.
"Can you rewrite it using nested ifs instead?"
# sure i guess why not.

#BONUS
if score >= 0 and score <= 100:
    if score >= 60:
        if score >= 70:
            if score >= 80:
                if score >= 90:
                    print("Your grade is A.")
                else:
                    print("Your grade is B.")
            else:
                print("Your grade is C.")
        else:
            print("Your grade is D.")
    else: 
        print("You failed your exam!")
else:
    print("Invalid Score.")
# its just messy to look at.