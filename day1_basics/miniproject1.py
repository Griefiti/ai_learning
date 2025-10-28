#Mini Project: Café Checkout System
#TASKA - subtotal calculation

item1 = float(input("What is the price of your first item: "))
item2 = float(input("What is the price of your second item: "))
item3 = float(input("What is the price of your third item: "))
total = 0

if item1 >= 0 and item2 >= 0 and item3 >= 0:
    subtotal = item1 + item2 + item3
    total += subtotal

    #TASKB - discounts and tax

    # member discount
    member = input("Are you a member?(y/n): ") 
    if member.lower() == "y":
        member_discount = subtotal * 0.1
        total -= member_discount
    else:
        member_discount = 0

    # promo discount
    if total >= 50: 
        promo_discount = total * 0.05
        total -= promo_discount
    else:
        promo_discount = 0

    # taxes
    GST = total * 0.09
    total += GST 
    
    #TASKC - receipt

    dollar_width = len(str(round(total, 2)))
    max_width = 19 + dollar_width
    label_width = max_width - dollar_width - 1

    print(f"{'<RECEIPT>':=^{max_width}}\n")
    print(f"{'Subtotal:':<{label_width}}${subtotal:>{dollar_width}.2f}")
    print(f"{'Member discount:':<{label_width}}${member_discount:>{dollar_width}.2f}")
    print(f"{'Promo discount:':<{label_width}}${promo_discount:>{dollar_width}.2f}")
    print(f"{'GST (9%):':<{label_width}}${GST:>{dollar_width}.2f}")
    print("-" * max_width)
    print(f"{'Total:':<{label_width}}${total:>{dollar_width}.2f}")
    
