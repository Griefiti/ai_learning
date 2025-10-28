#TASK1 - Lists
favourite_food = ["Fried_rice", "Fried_chicken", "Ramen", "Pizza", "Water"]
print(favourite_food[0])
print(favourite_food[-1])
favourite_food[2] = "Wonton_mee"
print(favourite_food)

'''How does list indexing work?'''
# The first item in a list always start with index zero. For example, item number 25 in a list would correspond to index 24. 
# If you wanted to call the last item in a list, you can use negative indexes. 
# -1 is the last item, -2 is the second to last. 
'''Why is Python's list powerful compared to individual variables?'''
# Lists can store multiple items, which can open up many different ways of using lists.
# Individual variables can sometimes feel lacking, being limited to only one item. 

#BONUS--------------------------------------------------------
natural_numbers = [1,2,3,4,5,6,7,8,9,10]

def add(a,b):
    return(a + b)

natural_numbers[9] = add(natural_numbers[4], natural_numbers[6])
print(natural_numbers)
# main issue right now, is getting the IndexError. 
# I dont know how to add an item to an already created list, without replacing an existing item.