nazv = []
kol = []
while True:
    print('=== ДНЕВНИК ТРЕНИРОВОК ===')
    print("1. Добавить")
    print("2. Показать все")
    print("3. Статистика")
    print("4. Выход")
    vib = input("Выбери: ")
    if vib == "1":
        tren = input("Какое упражнение? ")
        koli = int(input("Сколько раз? "))
        nazv.append(tren)
        kol.append(koli)
        print("Успешно добавлено!")
    elif vib == "2":
        if len(nazv) == 0:
            print("Пока нет тренировок")
        else:
            for i in range (len(nazv)):
                print(nazv[i], "-", kol[i], "раз")
    elif vib == "3":
        a = len(nazv)
        b = sum(kol)
        print(f"Всего тренировок - ", a, "Суммарно - ", b)
    elif vib == "4":
        print("Пока!")
        break
    else:
        print("Нет такого варианта!")




