import sys

if __name__ == '__main__':
    task = input('Write the task number: ')
    try:
        int(task)
    except ValueError:
        print('It is not number.')
        sys.exit()

    if task == '1':
        word1 = input('Write a number: ')
        try:
            if int(word1) > 7:
                print('Привет')
        except ValueError:
            print('It is not number.')
    elif task == '2':
        word2 = input('What is your name? ')
        if word2 == 'Вячеслав':
            print('Вячеслав')
        else:
            print('Нет такого имени')
    elif task == '3':
        word3 = input('Write an array of numbers: ')
        try:
            check1 = int(word3)
            f1 = list(word3)
            print('Array elements that are multiples of 3:')
            for i in f1:
                if int(i) % 3 == 0:
                    print(i)
        except ValueError:
            print('The array has not only numbers.')
    elif task == '4':
        # [((())()(())]]
        s = input('Введите скобочную последовательность: ')
        for i in s:
            if i != '[' and i != ']' and i != ')' and i != '(':
                print('В последовательности не только скобки!')
                sys.exit()

        counter1 = 0
        counter2 = 0
        for i in s:
            if i == '(':
                counter1 += 1
            elif i == ')':
                counter1 -= 1
            elif i == '[':
                counter2 += 1
            elif i == ']':
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
    else:
        print('We have only 4 tasks')
