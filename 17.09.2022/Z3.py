import sys
import pickle
import os
print("Падалко Богдан. Занятие-2.")
print("Рабочая директория:\n"+os.getcwd())
print("№7")
l1 = ["Inky", "Blinky", "Pinky", "Clyde"]
if os.path.exists("z3_output.pkl"):
    os.remove("z3_output.pkl")
    print("Старый файл z3_output.pkl удалён.")
f = open("z3_output.pkl", "w+b")
if f is None:
    print("Не удалось создать файл z3_output.pkl.")
    sys.exit()
print("Файл z3_output.pkl создан.")
pickle.dump(l1, f)
print("Список добавлен в файл z3_output.pkl.")
f.seek(0)
print("№8")
l2 = pickle.load(f)
print("Содержание файла z3_output.pkl:")
print(l2)
print("Тип: "+str(type(l2))+".")