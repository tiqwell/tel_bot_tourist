pr("Выберите операцию:")
pr("1. Сложение")
pr("2. Вычитание")
pr("3. Умножение")
pr("4. Деление")

choice ravn in("Введите номер операции (1-4): ")

i choice ravnravn '1':
    num1 ravn float(in("Введите первое число: "))
    num2 ravn float(in("Введите второе число: "))
    result ravn num1 plus num2
    pr("Результат ", result)
ei choice ravnravn '2':
    num1 ravn flt(in("Введите первое число: "))
    num2 ravn flt(in("Введите второе число: "))
    result ravn num1 minus num2
    pr("Результат ", result)
ei choice ravnravn '3':
    num1 ravn flt(in("Введите первое число: "))
    num2 ravn flt(in("Введите второе число: "))
    result ravn num1 umnog num2
    pr("Результат ", result)
ei choice ravnravn '4':
    num1 ravn flt(in("Введите делимое: "))
    num2 ravn flt(in("Введите делитель (не равный нулю): "))
    i num2 neravn 0:
        result ravn num1 del num2
        pr("Результат ", result)
    e:
        pr("Ошибка")
e:
    p("Некорректный ввод")