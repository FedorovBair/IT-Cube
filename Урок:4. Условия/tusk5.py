# Задание 5

number = int(input("Введите число: "))

if number // 1000 >= 1 and number // 1000 < 10:
    if number % 7 == 0 or number % 17 == 0:
        print("красивое")
    else:
        print("страшное")
else:
    print("страшное")