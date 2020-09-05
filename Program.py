"""Проверка чисел

Вариант 22
Написать программу, проверяющую, является ли введенное число
числом Нивена.
Если число не является числом Нивена, проверить является ли оно
множественным числом Нивена,
т.е. остаток от деления на сумму цифр дает другое число Нивена.

Множественным числом Нивена является 6804
6804/18 = 378, 378/18 = 21, 21/3 = 7, 7/7 = 1.

Входные значения: число. Выходные значения: сообщение по результатам
проверки для каждой системы счисления.

Примеры для работы программы:
6804 - Число Нивена
6505 - Множественное число
1a - Неверный ввод
0 - Недопустимое число
-111 - Недопустимое число
76 - Не число Нивена
e - Завершение работы

    python -m Program.py

:Authors:
    Чанчиков Сергей Александрович, КИ20-17/1Б

"""


def check(num, denom=None):
    """Функция проверяет остаток от деления
    Может принимать как 1 аргумент, так и 2
    При передаче 1-го аргумента - передаётся остаток от деления
    Если 2 - передаётся делимое и делитель соответственно
    """
    # Проверка на наличие 2-го аргумента
    if denom is None:
        if num == 0:
            return True
        return False
        # Проверка остатка от деления
    if num % denom == 0:
        return True
    return False


def get_denominator(num):
    """Функция вычисляет делитель
    Складывает цифры из каждого разряда числа
    """
    denominator = 0
    # Выполняем, пока в числе не останется цифр
    while num != 0:
        # Складываем
        denominator += num % 10
        # Уменьшаем количество разрядов
        num //= 10
    return denominator


def case_handler(uinput):
    # Объявляем переменную для числа
    num = 0

    # Пытаемся преобразовать строковый ввод в число
    try:
        num = int(uinput)
    except ValueError:
        # Если не получилось преобразовать str в int
        # То выводим соответствующее сообщение
        print("ERROR. I say NUMBER\n")
        return

    # Проверка числа
    # Если число меньше или равно 0
    # То число Нивена вычислить невозможно
    if num <= 0:
        # Если было введено недопустимое число
        # То выводим соответствующее сообщение
        print("Wrong number, print another number\n")
        return
    # Вычисляем знаменатель
    denominator = get_denominator(num)
    # Вычисляем остаток от деления
    remainder = num % denominator

    # Передаём право на проверку функции check
    if check(remainder):
        # Выводим результат проверки
        print(uinput + " - the Niven number\n")
    else:
        # Проверяем, является ли число множестенным числам Нивена
        if check(remainder, get_denominator(remainder)):
            print(uinput + " - the plural Niven number\n")
        else:
            print(uinput + " - not a Niven number\n")


def main():
    # Зациклим программу для беспрерывной работы
    while True:
        # Получаем ввод
        uinput = input("Print number\n")
        # Проверяем, является ли ввод командой для завершения работы
        # Если да, то прощаемся и завершаем цикл
        if uinput == "e":
            print("Goodbye!")
            break
        # В ином случае переходим к основной логике
        case_handler(uinput)
if __name__ == '__main__':
    """
    Точка входа в программу, необходим для корректного
    запуска с помощью команды:
        python -m Program.py
    """
    print("Print e for exit")
    main()