print("Hello world")
auto = "bmw".upper()
auto1 = "audi".upper()
auto2 = "mazda".upper()
auto3 = "honda".upper()
auto4 = "toyota".upper()
auto5 = "ford".upper()
auto6 = "porsche".upper()
print("Я хочу иметь в своем гараже семь машин : {}, {}, {}, {}, {}, {}, {}".format(auto, auto1, auto2, auto3, auto4, auto5, auto6))

answer = input("Готов перейти к вычислениям?(Y/N)?")
if answer == "Y":
    a = input("Тогда перейдем к делу.\n - 1 умножение \n - 2 деление \n - 3 слложение \n - 4 вычитание \n - 5 покинуть программу \n Выберите цифру:")
    if a == "1":
        b = int(input("Введите первое значение"))
        с = int(input("Введите второе значение"))
        print("Ответ", b * c)
    elif a == "2":
        b = int(input("Введите перввое значение"))
        c = int(input("Введите второе значение"))
        print("Ответ", b / c)
    elif a == "3":
        b = int(input("Введите первое значение"))
        c = int(input("Введите второе значение"))
        print("Ответ", b + c)
    elif a == "4":
        b = int(input("Ввведите первое значение"))
        c = int(input("Введите второе значение"))
        print("Ответ", b - c)
    elif  a== "5":
        print("До новвых встреч")
elif answer == "N":
    print("Удачи")
else:
    print("Неизвестный символ")



