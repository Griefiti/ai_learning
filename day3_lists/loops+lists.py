fruits = ["grapes", "banana", "avocado", "mango", "pineapple"]
for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(i, fruits[i])

#TASK2 Loop Practice
games = ["C&C-generals", "Mobile legends", "Valorant", "Omori", "Subway Surfers"]
for g in games:
    print(g)

print()

for g in range(len(games)):
    print(f"My number {g+1} favourite game is {games[g]}")

'''When should I use for item in list vs. for i in range(len(list))?'''
# We use the first we're trying to print the seperate items in a list. The latter is when you also need to print the indexes as well.
'''Which one feels more “Pythonic”?'''
# I'm not sure what you mean by "Pythonic" but I guess the second one.
# I just searched it up, apparently it means easy to read and write in python. Then the answer has to be the first one.
# It just intuitively pulls out an item from the list without the need for range() or len()

#BONUS------------------------------------------------------------------------------
names = ["Amelia", "Paras", "Jackson"]
age = [23, 31, 56]
person = [names, age]
for i in range(3):
    print(f"Id number:{i+1}")
    for j in range(2):
        if j == 0:
            print(f"Name is {person[j][i]}.")
        else:
            print(f"The person is {person[j][i]} years old.")
# I tried meshing lists and extracting an item from inside a list in a list. 
# It works!! WOOHOO.