import os
import sys
print("Падалко Богдан. Занятие-2.")
print("Рабочая директория:\n"+os.getcwd())
print("№4")
if os.path.exists("z2_cat"):
    print("Каталог z2_cat существует.")
else:
    os.mkdir("z2_cat")
    if not os.path.exists("z2_cat"):
        print("Не удалось создать каталог z2_cat.")
        sys.exit()
    print("Каталог z2_cat создан.")
input("Нажмите Enter для продолжения работы.")
if not os.path.exists("z2_cat/z2_output.txt"):
    f = open("z2_cat/z2_output.txt", "a+")
    if f is None:
        print("Не удалось создать файл z2_cat/z2_output.txt.")
        sys.exit()
    print("Файл z2_cat/z2_output.txt создан.")
    f.close()
else:
    print("Файл z2_cat/z2_output.txt существует.")
input("Нажмите Enter для продолжения работы.")
print("№5")
os.rename("z2_cat/z2_output.txt", "z2_cat/z2_output_new.txt")
if os.path.exists(r"z2_cat\z2_output_new.txt"):
    print("Файл переименован в z2_cat/z2_output_new.txt.")
else:
    print("Ошибка при переименовании в z2_cat/z2_output_new.txt.")
    sys.exit()
input("Нажмите Enter для продолжения работы.")
print("№6")
os.remove("z2_cat/z2_output_new.txt")
if not os.path.exists("z2_cat/z2_output_new.txt"):
    print("Файл z2_cat/z2_output_new.txt удалён.")