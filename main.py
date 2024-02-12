print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1-4): ")

if choice == '1':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 + num2
    print("Результат ", result)
elif choice == '2':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 - num2
    print("Результат ", result)
elif choice == '3':
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    result = num1 * num2
    print("Результат ", result)
elif choice == '4':
    num1 = float(input("Введите делимое: "))
    num2 = float(input("Введите делитель (не равный нулю): "))
    if num2 != 0:
        result = num1 / num2
        print("Результат ", result)
    else:
        print("Ошибка")
else:
    print("Некорректный ввод")