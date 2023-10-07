print("Подпункт А из ДЗ.")
счетчик_А = 1
while счетчик_А > 0:
    kА = int(input("Введите k (вертикаль первой фигуры): "))
    lА = int(input("Введите l (горизонталь первой фигуры): "))
    mА = int(input("Введите m (вертикаль второй фигуры): "))
    nА = int(input("Введите n (горизонталь второй фигуры): "))
    if kА < 0 or kА > 8 or nА < 0 or nА > 8 or lА < 0 or lА > 8 or mА < 0 or mА > 8:
        print("Проверьте правильность введенных координат (числа от 1 до 8).")
    else:
        print("Первая и вторая фигура на одном цвете." if (kА + lА + mА + nА) % 2 == 0 else "Первая и вторая фигура не на одном цвете.")
        счетчик_А -= 1


print("------------------------------------------")
print("Подпункт Б из ДЗ.")
счетчик_Б = 1
while счетчик_Б > 0:
    kБ = int(input("Введите k (вертикаль атакующей фигуры): "))
    lБ = int(input("Введите l (горизонталь атакующей фигуры): "))
    mБ = int(input("Введите m (вертикаль поля): "))
    nБ = int(input("Введите n (горизонталь поля): "))
    тип_атакующей_фигуры = str(input("Введите название атакующей фигуры (ферзь, ладья, слон, конь): "))
    if (kБ == mБ and lБ == nБ) or kБ < 0 or kБ > 8 or nБ < 0 or nБ > 8 or lБ < 0 or lБ > 8 or mБ < 0 or mБ > 8 or (тип_атакующей_фигуры != "ферзь" and тип_атакующей_фигуры != "ладья" and тип_атакующей_фигуры != "слон" and тип_атакующей_фигуры != "конь"):
        print("Проверьте правильность введенных данных.")
    else:
        if тип_атакующей_фигуры == "ферзь":
            if kБ == mБ or lБ == nБ or kБ - lБ == mБ - nБ or kБ + lБ == mБ + nБ:
                print("Ферзь представляет угрозу для этого поля.")
            else:
                print("Ферзь не представляет угрозу для этого поля.")

        elif тип_атакующей_фигуры == "ладья":
            if kБ == mБ or lБ == nБ:
                print("Ладья представляет угрозу для этого поля.")
            else:
                print("Ладья не представляет угрозу для этого поля.")

        elif тип_атакующей_фигуры == "слон":
            if kБ - lБ == mБ - nБ or kБ + lБ == mБ + nБ:
                print("Слон представляет угрозу для этого поля.")
            else:
                print("Слон не представляет угрозу для этого поля.")

        else: #тип атакующей фигуры КОНЬ
            if (abs(kБ - mБ == 1) and abs(lБ - nБ == 2)) or (abs(kБ - mБ == 2) and abs(lБ - nБ == 1)):
                print("Конь представляет угрозу для этого поля.")
            else:
                print("Конь не представляет угрозу для этого поля.")

        счетчик_Б -= 1


print("------------------------------------------")
print("Подпункт В из ДЗ.")
счетчик_В = 1
while счетчик_В > 0:
    kВ = int(input("Введите k (вертикаль атакующей фигуры): "))
    lВ = int(input("Введите l (горизонталь атакующей фигуры): "))
    mВ = int(input("Введите m (вертикаль поля): "))
    nВ = int(input("Введите n (горизонталь поля): "))
    тип_атакующей_фигуры_В = str(input("Введите название атакующей фигуры (ферзь, ладья, слон, конь): "))
    if (kВ == mВ and lВ == nВ) or kВ < 0 or kВ > 8 or nВ < 0 or nВ > 8 or lВ < 0 or lВ > 8 or mВ < 0 or mВ > 8 or (тип_атакующей_фигуры != "ферзь" and тип_атакующей_фигуры != "ладья" and тип_атакующей_фигуры != "слон" and тип_атакующей_фигуры != "конь"):
        print("Проверьте правильность введенных данных.")
    else:
        if тип_атакующей_фигуры_В == "ферзь":
            if kВ == mВ or lВ == nВ or kВ - lВ == mВ - nВ or kВ + lВ == mВ + nВ:
                print("Ферзь представляет угрозу для этого поля за один ход.")
            else:
                print("Ферзь не представляет угрозу для этого поля за один ход.")
                print("Ферзь представляет угрозу за два хода если сходит на клетку: вертикаль: " + str(
                    mВ) + ", горизонталь: " + str(lВ) + " или вертикаль: " + str(kВ) + ", горизонталь: " + str(
                    nВ) + ".")

        elif тип_атакующей_фигуры_В == "ладья":
            if kВ == mВ or lВ == nВ:
                print("Ладья представляет угрозу для этого поля за один ход.")
            else:
                print("Ладья не представляет угрозу для этого поля за один ход.")
                print("Ладья представляет угрозу за два хода если сходит на клетку: вертикаль: " + str(
                    mВ) + ", горизонталь: " + str(lВ) + " или вертикаль: " + str(kВ) + ", горизонталь: " + str(
                    nВ) + ".")

        elif тип_атакующей_фигуры_В == "слон":
            if kВ - lВ == mВ - nВ or kВ + lВ == mВ + nВ:
                print("Слон представляет угрозу для этого поля за один ход.")
            else:
                print("Слон не представляет угрозу для этого поля за один ход.")
                if (kВ + lВ + mВ + nВ) % 2 == 0:
                    for zВ in range(1,9):
                        for qВ in range(1,9):
                            if (abs(kВ - zВ) == abs(lВ - qВ)) and (abs(mВ - zВ) == abs(nВ - qВ)):
                                print("Слон представляет угрозу за два хода если сходит на клетку: вертикаль: " + str(zВ) + ", горизонталь: " + str(qВ) + ".")
                else:
                    print("Слон не представит угрозу для этого поля никогда...")

        else: #тип атакующей фигуры КОНЬ
            if (abs(kВ - mВ == 1) and abs(lВ - nВ == 2)) or (abs(kВ - mВ == 2) and abs(lВ - nВ == 1)):
                print("Конь представляет угрозу для этого поля за один ход.")
            else:
                print("Конь не представляет угрозу для этого поля за один ход.")
                n = 0
                for oВ in range(1,9):
                    for pВ in range(1,9):
                        if ((kВ - oВ)**2 + (lВ - pВ)**2 == 5) and ((mВ - oВ)**2 + (nВ - pВ)**2 == 5):
                            print("Конь представляет угрозу за два хода если сходит на клетку: вертикаль: " + str(oВ) + ", горизонталь: " + str(pВ) + ".")
                            n += 1
                if n == 0:
                    print("Конь не представляет угрозу для этого поля за два хода.")



        счетчик_В -= 1