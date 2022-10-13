import logger as log
import ui as ui
import operations as  oper


def button_click():
    a, b, ver = ui.ui()

    if ver == 3:
        print('Программа отменена')
        exit()

    operation = ui.oper()

    if operation == '*': result = oper.mult(a, b)
    elif operation == '/': result = oper.div(a, b)
    elif operation == '+': result = oper.sum(a, b)
    elif operation == '-': result = oper.diff(a, b)

    print(f"{a} {operation} {b} = {result}")
    log.loging(a, b, operation, result)
    button_click()