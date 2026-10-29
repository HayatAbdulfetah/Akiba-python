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
    try:
        total = calculate_subtotal(items)
        discount = calculate_discount(total)
        discounted_total = total - discount
        tax = calculate_tax(discounted_total, tax_rate)
        final_amount = discounted_total + tax
        
        # Formatted UI output
        print("\n======= SHOPPING RECEIPT =======")
        for item in items:
            item_total = item["price"] * item["quantity"]
            print(f'{item["name"]:<12} x {item["quantity"]:<3} {item_total:>12.2f} Birr')

        print("--------------------------------")
        print(f"Subtotal:         {total:>12.2f} Birr")
        print(f"Discount:        -{discount:>12.2f} Birr")
        print(f"After discount:   {discounted_total:>12.2f} Birr")
        print(f"Tax ({tax_rate*100:.0f}%):       +{tax:>12.2f} Birr")
        print("--------------------------------")
        print(f"Final amount:     {final_amount:>12.2f} Birr")
        print("================================\n")

        return {
            "subtotal": total,
            "discount": discount,
            "tax": tax,
            "final_amount": final_amount
        }
    except ValueError as e:
        print(f"\n[Receipt Error]: {e}\n")
        return None

# Valid Test Case
items = [
     {"name": "Notebook", "price": 80, "quantity": 3},
     {"name": "Pen", "price": 15, "quantity": 5}
]
generate_receipt(items, 0.15)
