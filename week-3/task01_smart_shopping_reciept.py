def calculate_subtotal(items):
    subtotal = 0
    for item in items:
        if item["price"] < 0 or item["quantity"] < 0:
            raise ValueError("Price and quantity cannot be negative.")
        total = item["price"] * item["quantity"]
        subtotal += total
    return subtotal

def calculate_discount(subtotal):
    if subtotal < 1000:
        discount = 0
    elif subtotal < 3000:
        discount = 0.05
    else: 
        discount = 0.1
    amount = subtotal * discount
    return amount

def calculate_tax(amount, tax_rate):
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")
    return amount * tax_rate

def generate_receipt(items, tax_rate):
    total = calculate_subtotal(items)
    discount = calculate_discount(total)
    discounted_total = total-discount
    tax = calculate_tax(discounted_total,tax_rate)
    final_amount = discounted_total+tax
    print("======= SHOPPING RECEIPT =======")

    for item in items:
        print(
            f'{item["name"]} x {item["quantity"]}: '
            f'{item["price"] * item["quantity"]:.2f} Birr'
        )

    print("--------------------------------")
    print(f"Subtotal:       {total:.2f} Birr")
    print(f"Discount:      -{discount:.2f} Birr")
    print(f"After discount: {discounted_total:.2f} Birr")
    print(f"Tax:             {tax:.2f} Birr")
    print("--------------------------------")
    print(f"Final amount:    {final_amount:.2f} Birr")
    print("================================")

    return {
        "subtotal": total,
        "discount": discount,
        "tax": tax,
        "final_amount": final_amount
    }

items = [
     {"name": "Notebook", "price": 80, "quantity": 3},
     {"name": "Pen", "price": 15, "quantity": 5}
 ]

generate_receipt(items, 0.15)
