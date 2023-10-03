def find_max_of_four(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
num4 = float(input("Введіть четверте число: "))

max_number = find_max_of_four(num1, num2, num3, num4)
print(f"Максимальне число: {max_number}")
