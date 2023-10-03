def draw_line():
    length = int(input("Введіть довжину лінії: "))
    direction = input("Введіть напрямок ('horizontal' або 'vertical'): ")
    character = input("Введіть символ: ")

    if direction == 'horizontal':
        line = character * length
    elif direction == 'vertical':
        line = '\n'.join(character for _ in range(length))
    else:
        print("Неправильний напрямок. Використовуйте 'horizontal' або 'vertical'.")
        return

    print(line)

draw_line()
