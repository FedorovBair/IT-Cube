# Задание 4

num1 = float(input())
num2 = float(input())
num3 = float(input())

sum_positive = 0

if num1 > 0:
    sum_positive += num1
if num2 > 0:
    sum_positive += num2
if num3 > 0:
    sum_positive += num3

print(sum_positive)