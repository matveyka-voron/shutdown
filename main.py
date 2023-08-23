import os, time, colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)

print(Fore.CYAN +
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|                                                                               |
|                  Приветствую тебя, дорогой пользователь!                      |
|                                                                               |
| Данная программа позволит тебе задать таймер до завершения работы компьютера. |
|                                                                               |
|                      Разработчик: Матвей Воронцов.                            |
|                                                                               |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print(Fore.LIGHTGREEN_EX + 'Приятного пользования! ;-)\n')

timee = 0
num = 0

while timee < 1 or timee > 3:
    try:
        timee = int(input('''В каких единицах будете вводить время для таймера?
    Секунды (1); Минуты (2); Часы (3).
    Введите цифру: '''))
        if timee < 1 or timee > 3:
            print('\nТребуется ввести число от 1 до 3!\n')
    except ValueError:
        print('\nОШИБКА!!! Вы ввели буквенное значение, а не число!\n')

if timee == 1:
    while num < 1:
        try:
            num = int(input("\nВведите количество секунд до завершения работы ПК: "))

            if num < 1:
                print('\nОШИБКА!!! Вы ввели значение меньше 0!\n')
        except ValueError:
            print('\nОШИБКА!!! Вы ввели буквенное значение, а не число!\n')
    num2 = num

    print('\n~~~~~~~~~~~~~~~~~~', Back.LIGHTWHITE_EX + Fore.RED + 'Хорошего дня? \,/(^_^)\,/' + Back.RESET + Fore.RESET, '~~~~~~~~~~~~~~~~~~\n')

    for i in range(num):
        if num2 % 60 != 0:
            print(Fore.RED + 'Ваш ПК самоуничтожится через:', num2, 'сек')
        else:
            print(Fore.RED + '\nВаш ПК самоуничтожится через секунд:', num2, '(' + str(int((num2) / 60)) + ' мин)\n')
        num2 = num2 - 1
        time.sleep(1)
elif timee == 2:
    while num < 1:
        try:
            num = int(input("\nВведите количество минут до завершения работы ПК: "))

            if num < 1:
                print('\nОШИБКА!!! Вы ввели значение меньше 0!\n')
        except ValueError:
            print('\nОШИБКА!!! Вы ввели буквенное значение, а не число!\n')
    num2 = num * 60

    print('\n~~~~~~~~~~~~~~~~~~', Back.LIGHTWHITE_EX + Fore.RED + 'Хорошего дня? \,/(^_^)\,/' + Back.RESET + Fore.RESET + ' ~~~~~~~~~~~~~~~~~~\n')

    for i in range(num * 60):
        if (num2) % 60 != 0:
            print(Fore.RED + 'Ваш ПК самоуничтожится через:', num2, 'сек')
        else:
            print(Fore.RED + '\nВаш ПК самоуничтожится через:', num2, 'сек', '(' + str(int((num2) / 60)) + ' мин)\n')
        num2 = num2 - 1
        time.sleep(1)
elif timee == 3:
    while num < 1:
        try:
            num = int(input("\nВведите количество часов до завершения работы ПК: "))

            if num < 1:
                print('\nОШИБКА!!! Вы ввели значение меньше 0!\n')
        except ValueError:
            print('\nОШИБКА!!! Вы ввели буквенное значение, а не число!\n')
    num2 = num * 3600

    print('\nДо выключения компьютера осталось часов:', num, '(' + str(num * 60) + ' мин., соответственно',(num * 60) * 60, ' сек)\n')

    for i in range(num * 3600):
        if (num2) % 60 != 0:
            print(Fore.RED + 'Ваш ПК самоуничтожится через:', num2, 'сек')
        else:
            print(Fore.RED + '\nВаш ПК самоуничтожится через:', num2, 'сек', '(' + str(int((num2) / 60)) + ' мин)\n')
        num2 = num2 - 1
        time.sleep(1)

os.system('shutdown /p /f')