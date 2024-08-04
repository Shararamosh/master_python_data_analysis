def sm(a = 1, b = 1, c = 1):
    return a+b+c, a*b*c
print("Позиционный способ вызова - sm(5, 6, 7):")
print(sm(5, 6, 7))
print("Именованный способ вызова - sm(a = 2, b = 3, c = 4):")
print(sm(a = 2, b = 3, c = 4))
print("Значение по умолчанию - sm():")
print(sm())
