'''
2. Користувач вводить два числа.
Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
'''

try:
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))

    if first_number == second_number:
        print('this numbers equal')
    else:
        max_number = max(first_number, second_number)
        min_number = min(first_number, second_number)
        print(f'{min_number}, {max_number}')
except ValueError:
    print('Please enter only integer numbers!')
