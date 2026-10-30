def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_divisors(number):
    if number <= 0:
        return []
    divisors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            divisors.append(divisor)
    return divisors

def sum_of_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total

def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10
    return reversed_number * sign

def analyze_number(number):
    divisors = get_divisors(number)
    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"
    return {
        "number": number,
        "parity": parity,
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": divisors
    }

# test yse the number 123
result = analyze_number(123)

print("======= NUMBER ANALYSIS =======")
print(f"Number: {result['number']}")
print(f"Parity: {result['parity']}")
print(f"Prime: {result['is_prime']}")
print(f"Sum of digits: {result['sum_of_digits']}")
print(f"Reversed number: {result['reversed_number']}")
print(f"Divisors: {result['divisors']}")
print("================================")
