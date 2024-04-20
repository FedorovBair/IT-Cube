# Задание 4

number = int(input("Введите трехзначное число: "))

a = number // 100
b = (number % 100) // 10
c = number % 10

print(number)              # abc
print(a, c, b, sep="")     # acb
print(b, a, c, sep="")     # bac
print(b, c, a, sep="")     # bca
print(c, a, b, sep="")     # cab
print(c, b, a, sep="")     # cba