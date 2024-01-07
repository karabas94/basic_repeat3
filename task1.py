"""
1. Користувач вводить із клавіатури номер дня тижня (1-7).
Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок, 2 — вівторок тощо.
"""

try:
    user_select = int(input('Please enter a number from 1 to 7: '))
    match user_select:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Incorrect menu item")
except ValueError as error:
    print('Enter only integer number please!')
