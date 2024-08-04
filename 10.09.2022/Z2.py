import sys
import math
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))
x = float(input("Введите x: "))
D = b*b-4*a*c
if D < 0:
    print("Дискриминант отрицательный - значение корня не будет выведено.")
else:
    y = -1.0*(b+math.sqrt(D))/2/a
    print("y_1 =", y)
y = math.pow(math.sin(x), 2)+math.log(abs(1+x), 2)
print("y_2 =", y)
