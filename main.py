def display_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))

min_num = min(num1, num2)
max_num = max(num1, num2)

display_odd_numbers(min_num, max_num)
