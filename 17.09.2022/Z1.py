import os
import sys
import random
import math
print("Падалко Богдан. Занятие-2.")
print("Рабочая директория:\n"+os.getcwd())
print("№1")
m = math.floor(abs(float(input("Введите правую границу промежутка m: "))))
if m == 0:
    print("Промежуток не может быть нулевым.")
    sys.exit()
n1 = int(input("Введите минимальное количество чисел n1: "))
n2 = int(input("Введите максимальное количество чисел n2: "))
if n2 <= 0:
    print("Некорректное максимальное количество чисел.")
    sys.exit()
if n1 < 0:
    n1 = 0
n = random.randint(n1, n2)
f = open("z1_output.txt", "a+")
if f is None:
    print("Не удалось открыть или создать файл z1_output.txt.")
    sys.exit()
if f.read(1):
    f.write("\n")
for i in range(n):
    if i != n-1:
        f.write("%d " % random.randint(-m, m))
    else:
        f.write("%d" % random.randint(-m, m))
f.seek(0)
print("Изменённый файл:\n"+f.read())
f.seek(0)
print("№2")
l = []
for line in f:
    l += map(int, line.split())
print("Строка чисел:"+" ".join(str(i) for i in l))
print("№3")
print("Список чисел:", l)
f.close()