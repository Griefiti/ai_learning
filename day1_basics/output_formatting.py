#TASK5 - formatting
price = 1233.546
print("price: $", price)

# f-strings
print(f"price: ${price:.2f}")     # precision
print(f"price: ${price:>13.3f}")  # alignment
print(f"{'price':<14}${price:,.1f}\n") # thousand grouping

"Why do we format numbers when printing instead of during calculation?"
# I think it is because the calculations will stop working entirely.
"What could happen if you round every value in between?"
# Starting from a slight deviation, you could end up with a very different result


#BONUS
chicken_strip = 9.55
cheese_burger = 14.60
fries = 5.00
total = chicken_strip + cheese_burger + fries

receipt_width = 21
dollar_width = len(str(total))
label_width = receipt_width - 1 - dollar_width

print(f"{'<RECEIPT>':=^{receipt_width}}\n")
print(f"{'chicken strip:':<{label_width}}${chicken_strip:>{dollar_width}.2f}")
print(f"{'cheese_burger:':<{label_width}}${cheese_burger:{dollar_width}.2f}")
print(f"{'fries:':<{label_width}}${fries:{dollar_width}.2f}")
print("-" * receipt_width)
print(f"{'total:':<{label_width}}${total:{dollar_width}.2f}")
