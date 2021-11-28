# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func_1(x,y):
        return f'{x} ^ {y} = {x**y}'
def my_func_2(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    return f'{x} ^ {y} = {1 / res}'
if __name__ == '__main__':
    x, y = int(input('Input first varaible')), int(input('Input second varaible'))
    if x > 0 and y < 0:
        print('my_func_1 = ' + my_func_1(x, y))
        print('my_func_2 = ' + my_func_2(x, y))
    else:
        print('invalid value')