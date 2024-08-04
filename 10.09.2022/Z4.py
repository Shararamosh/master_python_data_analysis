import sys
n = int(input("Введите натуральное число: "))
if n <= 0:
    print("Введённое число не является натуральным.")
    sys.exit()
h0 = False
h5 = False
b = True
while b and n > 0:
    k = n%10
    if k == 0:
        h0 = True
    elif k == 5:
        h5 = True
    n = n//10
    if h0 and h5:
        b = False
if b:
    print("В записи числа нет одновременно цифр 0 и 5.")
else:
    print("В записи числа есть одновременно цифры 0 и 5.")
