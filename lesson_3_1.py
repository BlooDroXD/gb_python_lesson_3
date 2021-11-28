# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        print('Ошибка при делении на 0')
if __name__ == '__main__':
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    print(f'{a} / {b} = {division(a,b)}')