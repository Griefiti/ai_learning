def subtract(a,b):
    return a - b 
    
a = int(input("Num1? "))
b = int(input("Num2? "))
answer = subtract(a,b)
print(answer)

#TASK4A - Simple Greeting
def welcome():
    print("Welcome to the Cafe Checkout System!")

welcome()

#TASK4B - Area Calculator
def area_rectangle(length,width):
    return length * width

print(f"{area_rectangle(23,14)}cm2")

#TASK4C - Even or Odd Checker

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

for i in range(1,11):
    print(f"{i} is a {even_or_odd(i)} number.")

'''What's the difference between a function that prints vs. one that returns a value?''' 
# The only difference is one gets displayed onto the screen, and the other most often gets stored inside a variable for other purposes. 
'''Why might functions make your code easier to maintain or reuse later?'''
# Functions allow us to shrink down and easily manage large complex programs by allowing us to completely replace small repetitive parts with a function/mini program. Imagine, you have multiple characters in a video game, and all of them have the same basic attack. Instead of coding for all ten. You make a function for the basic attack and call the function in all ten characters.
# Its also much neat and tidier.

#BONUS-------------------------------------------------------------------------
def kinetic_energy(mass,velocity):
    return round(0.5 * mass * velocity**2,2)

def accident_equivalent(KE):
    if KE <= 12.5:
        Accident = "stubbing your toe with a table leg"
        Injury = "minor pain and redness"
    elif KE <= 85:
        Accident = "dropping a phone on your foot"
        Injury = "bruise or mild swelling"
    elif KE <= 325:
        Accident = "tripping and falling on flat ground" 
        Injury = "scrape, bruising, mild sprain"
    elif KE <= 1250:
        Accident = "getting hit by a baseball" 
        Injury = "bruising, possible fracture"
    elif KE <= 3500:
        Accident = "a bicycle crash at 15 km/h" 
        Injury = "road rash, possible fracture"
    elif KE <= 15000:
        Accident = "falling off a ladder (~2 m height)" 
        Injury = "fractured limb, concussion risk"
    elif KE <= 87500:
        Accident = "a motorbike collision (~50 km/h)" 
        Injury = "multiple fractures, internal bleeding"
    elif KE <= 325000:
        Accident = "a car crash (~80 km/h)" 
        Injury = "Severe trauma, organ damage"
    elif KE <= 500000:
        Accident = "getting hit by a truck (~100 km/h)" 
        Injury = "critical/fatal injuries"
    elif KE <= 1000000:
        Accident = "high-speed train impact (~250 km/h)" 
        Injury = "instant fatality"
    else:
        Accident = "getting your asian parents disappointed" 
        Injury = "EMOTIONAL DAMAGE"

    return Accident , Injury

#MAIN CODE
mass = 0
velocity = 0
while mass <= 0:
    mass = float(input("How heavy is the object (kg)? "))
while velocity <= 0:
    velocity = float(input("Give me a random speed (m/s)? "))

KE = kinetic_energy(mass, velocity)
Accident, Injury = accident_equivalent(KE)

print("<ACCIDENT ENERGY CALCULATOR>")
print(f"Approximately {KE}J of force was inflicted onto you")
print(f"The equivalent accident would be {Accident}.")
print(f"The injuries would be {Injury}. ")

