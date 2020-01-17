import os
import re
import requests
import numpy as np
import pandas as pd
from tqdm import tqdm

class req_num: # Класс, который хранит название требования/навыка и количество его повторений в вакансиях
    value = ''
    number = 0

    def __init__(self, value, number):
        self.value = value
        self.number = number

def get_vacancies_descriptions(specialization_number):
    vac = [] # [requests.get('https://api.hh.ru/vacancies?specialization={}'.format(specialization_number), params={'page': i, 'per_page':20}).json() for i in tqdm(range(0, 98), 'Формирование массива vac')]
    for i in tqdm(range(0, 98), 'Формирование массива vac'):
        vac.append(requests.get('https://api.hh.ru/vacancies?specialization={}'.format(specialization_number), params={'page': i, 'per_page':20}).json())

    pac = [] # Может быть можно записать в одну строчку
    for i in range(0, 39):
        for j in range(0, 20):
            pac.append(vac[i]['items'][j]['alternate_url'])

    lili = [re.sub(r'[^0-9]', '', e) for e in pac]

    vak_url = 'https://api.hh.ru/vacancies/{}'
    var = [requests.get(vak_url.format(i)).json() for i in tqdm(lili, 'Формирование массива var')]

    # Вывод всех описаний в файл, с помощью DataFrame
    # Теперь есть вывод в файл прямо из массива (функция write_to_csv), так что если DataFrame не нужен, как промежуточный массив, можно убрать эти строки
    # df = pd.DataFrame(var)
    # df['description'] = df['description'].apply(lambda x: (re.sub(r'<.*?>', '', str(x)))) # Теги HTML лучше не удалять, за них можно цеплятся с помощью регулярных выражений
    # df.to_csv('data/description.csv', columns =['description'])

    des = [i['description'] for i in var] # Можно возвращать сразу то, что справа от знака равно
    return des # Это для наглядности

def get_specializations():
    spec = [] # Список специализаций
    spec.append(requests.get('https://api.hh.ru/specializations').json())

    # Задача: выгруженный список отфильтровать от специальностей, не связанных со специализацией Программное и аппаратное обеспечение встраиваемых систем
    # Для специализации с Id=1.274

def get_regex(): # Функция для формирования регулярного выражения
    # Регулярное выражение формируется в соответсвии со словами из файлов словарей
    # Эти файлы можно заполнять с помощью сайтов поиска синонимов и т. п.

    # Начальное положение поиска
    regex_start = ''
    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/vacabulary_start.csv') as f_in:
        for line in f_in:
            regex_start += line.replace('\n', '') + '|'

    # Конечное положение поиска
    regex_end = ''
    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/vacabulary_end.csv') as f_in:
        for line in f_in:
            regex_end += line.replace('\n', '') + '|'

    # (?:Обязанности|Требования|Навыки|Ищем|Ищет|Ждем|Ждет).*?(?:Удобный|График|Желательно|Условия|<strong>|$.|\n)
    return re.compile('(?:' + regex_start[:-1] + ')' + '.*?' + '(?:' + regex_end[:-1] + ')')

def get_requirements(des): # Функция для поиска требований/навыков

    reqs = []

    # 1. Убираем лишний текст из файла с описанием вакансий, с помощью регулярного выражения get_regex()

    for i in des:
        temp = ''
        for j in get_regex().findall(i, re.IGNORECASE): # Выборка блоков, соответствующих регулярному выражению
            temp += str(j)
        reqs.append(temp)

    # 2. Собираем вакансии в массив, разделители: (,|.|;) или (<li>.*?<\/li>)

    req = []
    for i in reqs:
        for j in re.findall(r'<li>.*?<\/li>', i): # re.findall(r'(?:<li>|,|\.|;).*?(?:\/li|,|\.|;)', i)
            req.append(re.sub(r'^ +', '', re.sub(r'<.*?>', '', str(j)).capitalize()))

    # Продумать разбор сложных предложений
    # *. Переделываем вакансии в общие формы (именительный падеж и т. п.)
    # *. Обработка сложных предложений с помощью алгоритмов или с помощью машинного обучения
    # Или можно просто выбирать по ключевым слова (языки программирования (С/С++), технологии (Git)), но тогда надо делать словари для всех специальностей

    # 3. Считаем количество совпадений, записываем в массив
    # 4. Записываем требования/навыки в файл в порядке убывания, файл называем номером_названием специальности

    return req # Возвращается массив, содержащий требования/навыки (элементы массива - req_num) и количество для повторяющихся

def write_to_csv(arr, file_name):
    try:
        f_out = open(os.path.dirname(os.path.abspath(__file__)) + '/data/' + file_name + '.csv', 'w')
        f_out.write('Number;"' + file_name.replace('_', ' ') + '"\n')
        for i in range(len(arr)):
            f_out.write(str(i) + ';' + '\"' + arr[i] + '\"' + '\n')
        f_out.close()
    except IOError:
        print('Error: could not open file!')

if __name__ == "__main__":
    pass