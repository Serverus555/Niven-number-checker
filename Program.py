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


def check(num, denom):
    if num % denom == 0:
        return True
    return False


def get_denominator(num):
    denominator = 0
    while num != 0:
        denominator += num % 10
        num //= 10
    return denominator


def case_handler(uinput):
    num = 0
    try:
        num = int(uinput)
    except ValueError:
        print("ERROR. I say NUMBER\n")
        return
    if num < 0:
        print("Wrong number, print natural number\n")
        return
    denominator = get_denominator(num)
    if denominator == 0:
        print("Wrong number, print another number\n")
        return

    if check(num, denominator):
        print(uinput + " - the Niven number\n")
    else:
        remainder = num % denominator
        if check(remainder, get_denominator(remainder)):
            print(uinput + " - the plural Niven number\n")
        else:
            print(uinput + " - not a Niven number\n")


def main():
    while True:
        uinput = input("Print number\n")
        if uinput == "e":
            print("Goodbye!")
            break
        case_handler(uinput)
if __name__ == '__main__':
    print("Print e for exit")
    main()