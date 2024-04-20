# Задание 1

number = int(input("Введите число: "))

before_numbers = list(range(number-3, number))
after_numbers = list(range(number+1, number+4))

result = ", ".join(str(i) for i in before_numbers + [number] + after_numbers)
print(result)