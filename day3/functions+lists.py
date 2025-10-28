def tripler(nums):
    for i in range(len(nums)):
        nums[i] *= 3
    return nums

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tripler(numbers))

print()
#TASK3 - Function + List Combo
def exponent(digits):
    for i in range(len(digits)):
        c_digits = digits[:]
        c_digits[i] = digits[i] ** 3
    return c_digits

integers = [2, 3, 4, 5, 8, 9, 10]
print(integers)
print(exponent(integers))
print()

'''What happens if you change the list inside the function?'''
# Lists are mutable. 
# Therefore, if you change the list inside the function, the original list will also be changed.
'''How can you avoid modifying the original list?'''
# You can create a copy of the original list under another name and modify the copy.

#BONUS------------------------------------------------------------------
def mental_check(io):
    print()
    good = 0
    for i in range(len(io)):
        if io[i] == healthy[i]:
            good += 1
    if good >= 4:
        print("You are a mentally stable person. Have a wonderful rest of the day!")
    else:
        print("Our readings indicate that you should check in with a doctor or therapist.")
        print("You can always call 646-274-126 for any question or concern you may have.")
    

questions = ["Would you say that you are currently happy with your lifestyle? (yes/no) ", "Have you been feeling loneliness, anxiety or insecure lately? (yes/no) ", "Have you had a chat with any of your family members or friends recently? (yes/no) ", "Have you done all of these activities this past year(smoking, drugs, gambling)? (yes/no) ", "Are you drowning in regrets about things you did or did not do?(yes/no) "]
healthy = ["yes", "no", "yes", "no", "no"]    

def mental_ask():
    answer = list() 
    for i in range(5):  
        quote = input(questions[i])
        answer.append(quote)
    return answer

print("<MENTAL HEALTH QNA>")
mental_check(mental_ask())
# At first i was going to check if you're mentally healthy if you said yes four or more times.
# However, i noticed half way through while making the questions that you could make negative questions where the response yes would be considered mentally unstable.
# Therefore, i created another list called healthy which contains answers which are correct/what a mentally sound person would say.
# Then all I had to do, was compare the results/inputs from the user with the values from that list.