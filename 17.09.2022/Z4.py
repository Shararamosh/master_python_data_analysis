import math
class VectorStartEnd:
    def __init__(self, x1 = 0.0, y1 = 0.0, z1 = 0.0, x2 = 0.0, y2 = 0.0, z2 = 0.0):
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

    def length(self):
        return math.sqrt(math.pow(self.x2-self.x1, 2)+math.pow(self.y2-self.y1, 2)+math.pow(self.z2-self.z1, 2))

    def __add__(self, other):
        return VectorStartEnd(self.x1+other.x1, self.y1+other.y1, self.z1+other.z1, self.x2+other.x2, self.y2+other.y2,
                              self.z2+other.z2)

    def __sub__(self, other):
        return VectorStartEnd(self.x1 - other.x1, self.y1 - other.y1, self.z1 - other.z1, self.x2 - other.x2,
                              self.y2 - other.y2, self.z2 - other.z2)

    def __mul__(self, other):
        return (self.x2-self.x1)*(other.x2-other.x1)+(self.y2-self.y1)*(other.y2-other.y1)+(self.z2-self.z1)*(other.z2-other.z1)

    def cos(self, other):
        return (self*other)/self.length()/other.length()

    def __str__(self):
        return "("+"("+str(self.x1)+", "+str(self.y1)+", "+str(self.z1)+")"+", "+"("+str(self.x2)+", "+str(self.y2)+", "+str(self.z2)+")"+")"


print("Падалко Богдан. Занятие-2.")
print("№(2)")
a = VectorStartEnd(1, 2, 3, 10, 9, 8)
b = VectorStartEnd(15, 16, 17, 20, 21, 22)
print("Даны векторы:")
print(a)
print(b)
print("Сумма векторов:")
print(a+b)
print("Разность векторов:")
print(a-b)
print("Скалярное произведение векторов:")
print(a*b)
print("Косинус угла между векторами:")
print(a.cos(b))