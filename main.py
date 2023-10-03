def sum_numbers_in_range(start, end):
    total = 0
    for number in range(start, end + 1):
        total += number
    return total

start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

result = sum_numbers_in_range(start, end)
print(f"Сума чисел у діапазоні від {start} до {end}: {result}")
