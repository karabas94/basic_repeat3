'''
3. Користувач вводить два числа та матем дію: + - * або /
Залежно від введеної матем дії вивести результат
'''

try:
    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))

    user_choice = int(input('Menu:\n1.Addition\n2.Subtraction\n3.Multiply\n4.Divide\nEnter your choice: '))

    match user_choice:
        case 1:
            print(f'Result: {first_number + second_number}')
        case 2:
            print(f'Result: {first_number - second_number}')
        case 3:
            print(f'Result: {first_number * second_number}')
        case 4:
            print(f'Result: {first_number / second_number}')
        case _:
            print("You can't select only from 1 to 4")
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Enter only integer number please!")
except Exception as error:
    print(f"Error: {error}")
