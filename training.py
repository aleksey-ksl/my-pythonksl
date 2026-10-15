titles = []
count = []
while True:
    print('=== ДНЕВНИК ТРЕНИРОВОК ===')
    print("1. Добавить")
    print("2. Показать все")
    print("3. Статистика")
    print("4. Выход")
    print("5. Подсчет индекса массы тела ИМТ")
    vib = input("Выбери: ")
    if vib == "1":
        tren = input("Какое упражнение? ")
        counts = int(input("Сколько раз? "))
        titles.append(tren)
        count.append(counts)
        print("Успешно добавлено!")
    elif vib == "2":
        if len(titles) == 0:
            print("Пока нет тренировок")
        else:
            for i in range (len(titles)):
                print(titles[i], "-", count[i], "раз")
    elif vib == "3":
        a = len(titles)
        b = sum(count)
        print("Всего тренировок - ", a, "Суммарно - ", b)
    elif vib == "4":
        print("Пока!")
        break
    elif vib == "5":
        rost = int(input("Ваш рост? "))
        weight  = int(input("Ваш вес? "))
        rost = rost / 100
        a = rost * rost
        imt = weight / a
        if imt <= 18.5:
            print(f"Недостаточная масса тела.  ИМТ: {imt:.1f}")
        elif imt <= 24.9:
            print(f"Нормальный вес! ИМТ: {imt:.1f}")
        elif imt <= 29.9:
            print(f"Избыточный вес. ИМТ: {imt:.1f}")
        elif imt <= 34.9:
            print(f"Ожирение | степени! ИМТ: {imt:.1f}")
        elif imt <= 39.9:
            print(f"Ожирение || степени!! ИМТ: {imt:.1f}")
        elif imt > 39.9:
            print(f'Ожирение ||| степени!!! ИМТ: {imt:.1f}')
    else:
        print("Нет такого варианта!")




