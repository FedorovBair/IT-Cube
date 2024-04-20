# Задание 3

students = int(input("Введите количество школьников: "))

mandarins = int(input("Введите количество мандаринов: "))

mandarins_per_student = mandarins // students
remainder = mandarins % students

print(mandarins_per_student)
print(remainder)