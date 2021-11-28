#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(var_1,var_2,var_3):
    if var_1 >= var_3 and var_2 >= var_3:
        return f'{var_1} + {var_2} = {var_1 + var_2}'
    elif var_1 > var_2 and var_1 < var_3:
        return f'{var_1} + {var_3} = {var_1 + var_3}'
    else:
        return f'{var_2} + {var_3} = {var_2 + var_3}'
if __name__ == '__main__':
    print(f'Result - {my_func(int(input("enter first variable ")), int(input("enter second variable ")), int(input("enter third variable ")))}')