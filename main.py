def is_happy_six_digit_number(number):
    if not isinstance(number, int) or number < 100000 or number > 999999:
        return False

    digits = [int(digit) for digit in str(number)]

    if sum(digits[:3]) == sum(digits[3:]):
        return True
    else:
        return False

num = int(input("Введіть шестизначне число: "))

if is_happy_six_digit_number(num):
    print(f"{num} є щасливим шестизначним числом.")
else:
    print(f"{num} не є щасливим шестизначним числом.")
