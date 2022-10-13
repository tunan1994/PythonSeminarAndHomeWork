from datetime import datetime as dt

def loging(arg1, arg2, operation, result):
    path = 'logger.txt'
    time_sign = dt.now().strftime('%D %H:%M')
    f = open(path, 'a')
    f.write(f'{time_sign}--> {arg1} {operation} {arg2} = {result}\n')
    f.close()