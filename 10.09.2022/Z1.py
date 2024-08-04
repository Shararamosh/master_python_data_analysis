import sys
n = int(input("Введите число: "))
if n <= 0:
    print("Число не натуральное.")
    sys.exit()
s = 0
while n > 0:
    s = s+(n%10)
    n = n//10
print("Сумма цифр числа:", s)
