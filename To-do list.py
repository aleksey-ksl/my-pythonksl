while True:
    print("ДНЕВНИК ДЕЛ \n"
          "1. Записать новое дело \n"
          "2. Посмотреть весь список \n"
          "3. Удалить весь список \n")
    a = int(input("Выбери цифру "))
    if a == 1:
        delo = input("Что произошло сегодня? ")
        with open("text.txt", "a", encoding="utf-8") as file:
            file.write("- " + delo + "\n")
            print("Успешно записано! ")
    elif a == 2:
            with open("text.txt", "r", encoding="utf-8") as file:
                print(file.read())
    elif a == 3:
        with open("text.txt", "w", encoding="utf-8") as file:
            pass
    else:
        print("Введите коректное число! ")








