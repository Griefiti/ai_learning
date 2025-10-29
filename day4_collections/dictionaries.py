#TASK3 - Dictionaries
person = {"name" : "Smithers", "job" : "firefighter", "age" : 27, "wife" : "Maria"}
print(person["name"])
person["job"] = "neurosurgeon"
person["address"] = "42 blockwood Ave"
del person["wife"]

print(person)
for k,v in person.items():
    print(v , k)
for c in person:
    print(c)
print()
'''Dictionaries are useful for _____ because _____.'''
# databases and storing related information because dictionaries can store pairs of data
'''Compared to lists and sets, they allow me to _____.'''
# store different datatypes which is very useful is some cases.
# Dictionaries are best for data that has a clear label–value relationship, like membership tiers or player scores.

#BONUS-------------------------------------------------------------------
#membership-tier list
tierlist = {"tier1" : 50, "tier2" : 23, "tier3" : 4}

def matching(t):
    for c in tierlist:      # had a hard time trying to unpack this damn dictionary
        if t in c:
            match c:
                case "tier1":
                    tierlist["tier1"] += 1
                case "tier2":
                    tierlist["tier2"] += 1
                case "tier3":
                    tierlist["tier3"] += 1

def matching_improved(num):
    key = f"tier{num}"
    if key in tierlist:
        tierlist[key] += 1
        print(f"Added 1 membership to {key.capitalize()}.")

while True:
    tier = input("What tier membership would you like to buy?(1-3) ")
    if tier not in ['1','2','3']:
        print("invalid number(1-3).")
        continue

    matching_improved(tier)
        
    again = input("Would you like to buy another membership?(yes/no) ")
    if again == "no":
        break

print("Final Summary")
for tier, number in tierlist.items():
    print(f"{tier.upper()}: {number}.")
# made the first thing that came to mind. Its kinda clunky though.
