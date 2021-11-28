#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

import re

def info_person(name, s_name, b_year, city, email, phone):
    valid_phone=re.sub(r'(\d{1})(\d{3})(\d{3})(\d{2})(\d{2})', r'\1-\2-\3-\4-\5', phone)
    return f'Name is : {name}, second name is : {s_name}, year of birth is: {b_year},' \
           f'City of residence is: {city}, email is : {email}, phone is : {valid_phone}'

if __name__ == '__main__':
    try:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        name = input('input name : ')
        second_name = input('input second name : ')
        year = int(input('input year of birth : '))
        city = input('input city of residence : ')
        email = input('input email : ')
        phone = input('input phone number (e.g. 89999999999) : ')
        if (re.fullmatch(regex, email) and len(phone) == 11):
            print('Info about person : ' + info_person(name=name, s_name=second_name, b_year=year, city=city, email=email, phone=phone))
        else:
            print('Invalid phone or email')
    except ValueError:
        print('invalid Value')