import random
a = 1
b = 10
p = 3
n = random.randint(a, b)
print("Загадано целое число от "+str(a)+" до "+str(b)+". На разгадку дано "+str(p)+" попытки.")
b = True
k = 0
while b and k < p:
    l = int(input("Ответ: "))
    if n == l:
        print("Верно!")
        b = False
    else:
        if n < l:
            print("Неверно! Загаданное число меньше.")
        else:
            print("Неверно! Загаданное число больше.")
        k = k+1
        if (k >= p):
            print("Попытки закончились.")
        else:
            print("Осталось попыток: "+str(p-k)+".")
