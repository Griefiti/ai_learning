# Mini-Project: Menu-Driven List Manager
#TASKA: Project Boot
items = []
total_width = 16
label_width = total_width - 9
count = 0
options = ["Add", "List", "Update", "Remove", "Search", "Sort", "Exit"]

def add_item():
    global count
    while True:
        while True:
            add = input("What item would you like to add to the list? ")
            if count > 0:                                                        
                if add.lower() in [item.lower() for item in items]:
                    print("Item already in the list!") 
            else:
                break

        items.append(add) 
        count += 1

        add_again = input("Would you like to add again?(yes/no) ")
        if add_again == "no":
            break
def list_item():
    if items == []:
        print("You haven't added anything to the list!")
    else:
        print(f"{'List':-^{total_width}}")
        for i in range(len(items)):
            print(f"{i+1})", items[i])
    global count
    print(f"You have {count} items in the list.")
def update_item():
    while True: 
        list_item()
        if items == []:
            break
        while True:
            update_index = input(f"Which item would you like to replace?(1-{len(items)}) ") #VALIDATION CHECK
            if update_index.isdigit():
                update_index = int(update_index)
                if 1 <= update_index <= len(items):
                    break
            else: 
                print("invalid index!")

        update = input("What would you like to replace it with: ")
        replaced = items[update_index - 1]
        print("Removed item: ", replaced)
        print("Updated item: ", update)

        confirmation = input("Please type 'yes' to confirm: ") # Checking for Confirmation
        if confirmation == "yes":
            items[update_index-1] = update
        update_again = input("Would you like to update again?(yes/no) ")
        if update_again == "no":
            break    
def remove_item():
    while True: 
        list_item()
        if items == []:
            break
        while True:
            remove_index = input(f"Which item would you like to remove?(1-{len(items)}) ") #VALIDATION CHECK
            if remove_index.isdigit():
                remove_index = int(remove_index)
                if 1 <= remove_index <= len(items):
                    break
            else: 
                print("invalid index!")

        print("Removed item: ", items[remove_index - 1])

        confirmation = input("Please type 'yes' to confirm: ") # Checking for Confirmation
        if confirmation == "yes":
            del items[remove_index - 1]
        remove_again = input("Would you like to remove again?(yes/no) ")
        if remove_again == "no":
            break
def search_item():
    found = False
    search = input("What item are you looking for? ")
    for i in range(len(items)):
        if search.lower() in items[i].lower():
            print(f"We found '{search}' in {items[i]} at number {i+1}.")
            found = True

    if not found:
        print("No match found.")
def sort_item():
    if items == []:
        print("You haven't added anything to the list!")
    else: 
        while True:
            sorting = input("Would you like to sort it from 'A-Z' or 'Z-A': ")
            if sorting == "A-Z" or sorting == "Z-A":
                break
            else:
                print("Please pick between 'A-Z' and 'Z-A'.")
        if sorting == "A-Z":
            A_Z()
        else:
            Z_A()

        list_item()
def A_Z(): # Selection Sort
    i = 0
    n = len(items)
    while i < n:
        min_index = i
        j = 0
        j += i
        while j < n:
            if items[j].lower() < items[min_index].lower() :
                min_index = j       
            j += 1
        items[min_index], items[i] = items[i], items[min_index]
        i += 1
def Z_A(): # Bubble Sort
    i = 1
    n = len(items)
    while i < n:
        j = 0
        while j < n - i:
            if items[j].lower()  < items[j + 1].lower() :
                items[j], items[j + 1] = items[j + 1], items[j]      
            j += 1
        i += 1
def exit():
    print("Exiting program... GOODBYE!")
    
def logic(ans):
    match ans:
        case "1":
            add_item()
        case "2":
            list_item()
        case "3":
            update_item()
        case "4":
            remove_item()
        case "5":
            search_item()
        case "6":
            sort_item()
        case "7":
            exit()
        case _:
            print("Please only type a number from 1 to 7!")

def main_menu():
    while True:
        print(f"\n{'<Main Menu>':=^{total_width}}")
        for i in range(len(options)):
            print(f"Option {i+1}:{options[i]:>{label_width}}")
        answer = input("Please select an option(1-7): ")
        print()
        logic(answer)
        if answer == "7":
            break

main_menu()

