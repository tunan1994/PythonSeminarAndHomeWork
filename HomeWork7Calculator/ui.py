import check as ch


def ui():
    mode = ch.check_mode('\n1 - Работа с рациональными числами;\n2 - Работа с комплексными числами;\n3 - Завершение работы;\nВвод ')
    if mode == 1:
        a = ch.check_float_number('Введите первое число ')
        b = ch.check_float_number('Введите второе число ')
    elif mode == 2:
        a = ch.check_complex_number('Введите первое число ')
        b = ch.check_complex_number('Введите второе число ')
    elif mode == 3:
        a = 0
        b = 0
    return a, b, mode

def oper():
    operation = ch.check_operation('Выберите арифметическое действие: "+", "-", "*", "/"\nВвод  ')
    return operation