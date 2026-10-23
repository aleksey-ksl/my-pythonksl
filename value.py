while True:
    print("Кошелек! \n "
          "1. Добавить расход \n "
          "2. Посмотреть все расходы \n "
          "3. Выход")
    try:
        a = int(input("Выбери цифру! - "))
        if a == 1:
            name = input("Название - ")
            summa = int(input("Сумма - "))
            with open("kosh.txt", "a", encoding="utf-8") as file:
                file.write(name + " - " + str(summa) + "\n")
            print("Расход успешно записан!")
        elif a == 2:
            try:
                itog = 0
                with open("kosh.txt", "r", encoding="utf-8") as file:
                    for line in file:
                        line = line.strip()
                        if not line:
                            continue
                        parts = line.split(" - ")
                        print(parts[0].strip(), "-", parts[1].strip(), "Р")
                        itog += int(parts[1].strip())
                print(f"Всего потрачено: {itog}Р ")
            except FileNotFoundError:
                print("Расходов пока нет! ")
        elif a == 3:
            break
        else:
            print("Нет такого варианта!")
    except ValueError:
        print("Введите цифру!")


