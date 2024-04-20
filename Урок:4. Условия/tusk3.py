# Задание 3

number1 = float(input("Введите первое число: "))
number2 = float(input("Введите второе число: "))
number3 = float(input("Введите третье число: "))
number4 = float(input("Введите четвертое число: "))

min_number = number1
if number2 < min_number:
    min_number = number2
if number3 < min_number:
    min_number = number3
if number4 < min_number:
    min_number = number4

print(f"{min_number}")