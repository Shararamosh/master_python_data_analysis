def getFirstNumber(n):
    return abs(n)%10
nl = [10, 20, 15, 20, 20, 11, 13, 20, 5, 11, -15, 20, 10, 20, 13]
nl.sort(key=getFirstNumber)
print("Сортировка по возрастанию младшей цифры:", nl)
nl.sort(key=getFirstNumber, reverse=True)
print("Сортировка по уменьшению младшей цифры:", nl)
