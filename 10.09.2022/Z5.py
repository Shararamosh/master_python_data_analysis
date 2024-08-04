s = 0
for n in range(1000, 10000):
    b = True
    while b and n > 0:
        if n%10 == 0:
            b = False
        n = n//10
    if not b:
        s = s+1
print("Четырёхзначных чисел, в которых присутствует 0: "+str(s)+".")
