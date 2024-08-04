def removeMaxFromList(l):
    ll = []
    m = l[0]
    for i in range(1, len(l)):
        if m < l[i]:
            m = l[i]
    for i in range(0, len(l)):
        if l[i] != m:
            ll.append(l[i])
    return ll
nl = [10, 20, 15, 20, 20, 11, 13, 20, 5, 11, -15, 20, 10, 20, 13]
print("Начальный список:", nl)
nll = removeMaxFromList(nl)
print("Конечный список:", nll)
