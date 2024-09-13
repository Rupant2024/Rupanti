def calculate_discount(purchase_amount):
    if purchase_amount > 100:
        discount_rate = 0.10
    else:
        discount_rate = 0.05

    discount_amount = purchase_amount * discount_rate
    return discount_amount

purchase_amount = float(input("Enter the purchase amount: $"))
discount_amount = calculate_discount(purchase_amount)

print(f"The discount amount is: ${discount_amount:.2f}")
