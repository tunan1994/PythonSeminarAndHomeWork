import logger as log

def check_float_number(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Ошибка. Введите рациональное число вида 1.11")
    return number

def check_complex_number(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = complex(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Ошибка. Введите комплексное число вида 1+1j")
    return number

def check_mode(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            if number in [1, 2, 3]:
                is_OK = True
            else:
                print("Ошибка. 1 - Рац.число; 2 - Комплексное число; 3 - Выход.")
        except ValueError:
            print("Ошибка. Введите число 1, 2 или 3")
    return number

def check_operation(inputText):
    operation_list = ['+', '-', '*', '/']
    is_OK = False
    while not is_OK:
        operation = input(f'{inputText}')
        if operation in operation_list:
            is_OK = True
            return operation
        else:
            print('Выберите верную операцию')