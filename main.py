import sys


def printPrivet():
    num1 = input('Write a number: ')
    if num1.isdigit():
        if int(num1) > 7:
            print('Привет')
    else:
        print('It is not number.')


def Vyacheslav():
    name = input('What is your name? ')
    if name == 'Вячеслав':
        print('Привет, Вячеслав')
    else:
        print('Нет такого имени')


def NumbersMultiples3():
    try:
        word3 = [int(el) for el in input('Write an array of numbers: ').split()]
        del3 = [i for i in word3 if i % 3 == 0]
        print(del3)
    except ValueError:
        print('Array has not only numbers!')


def Skobki():
    # [((())()(())]]
    sk_pos = input('Введите скобочную последовательность: ')
    for tek_sk in sk_pos:
        if tek_sk != '[' and tek_sk != ']' and tek_sk != ')' and tek_sk != '(':
            print('В последовательности не только скобки!')
            return False

    counter1 = 0
    counter2 = 0
    for tek_sk in sk_pos:
        if tek_sk == '(':
            counter1 += 1
        elif tek_sk == ')':
            counter1 -= 1
        elif tek_sk == '[':
            counter2 += 1
        elif tek_sk == ']':
            counter2 -= 1

        if counter1 < 0:
            print('Скобочная последовательность неправильная, не хватает круглой открывающей скобки')
        elif counter2 < 0:
            print('Скобочная последовательность неправильная, не хватает квадратной открывающей скобки')

    if counter1 == 0 and counter2 == 0:
        print('Скобочная последовательность правильная')
    elif counter1 != 0:
        print(
            'Скобочная последовательность неправильная. количество открывающих и закрывающих круглых скобок не равно')
    elif counter2 != 0:
        print(
            'Скобочная последовательность неправильная. количество открывающих и закрывающих квадратных скобок не равно')


if __name__ == '__main__':
    printPrivet()
    Vyacheslav()
    NumbersMultiples3()
    Skobki()
