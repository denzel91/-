first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
second_value: str = input('Input second value ')

for value in {first_value, second_value}:
    first_value: int = int(first_value)
    second_value: int = int(second_value)
    first_value: int = int(first_value)
    second_value: int = int(second_value)
    if operation == '+':
        print(first_value + second_value)
    elif operation == '-':
        print(first_value - second_value)
    elif operation == '/' and second_value:
        print(first_value / second_value)
    elif operation == '//' and second_value:
        print(first_value // second_value)
    else:
        print(f'Invalid operation {operation}')
        try:
            first_value: int = int(first_value)
            second_value: int = int(second_value)
        except ValueError:
            print('ERROR')
        except ZeroDivisionError:
            pass
        else:
            print('OK')
        finally:
            print('CLOSE')





