import os
import re
import requests
import numpy as np
import pandas as pd
from tqdm import tqdm
from collections import Counter

def get_specializations():
    spec = requests.get('https://api.hh.ru/specializations').json()

    regex = ''
    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/vacabulary_specializations.csv') as f_in:
        for line in f_in:
            regex += line.replace('\n', '') + '|'
    regex = '(?:' + regex[:-1] + ')'

    ids = []
    for i in spec:
        for j in i["specializations"]:
            if re.search(regex, j['name'], re.IGNORECASE):
                ids.append(j['id'])
    
    return ids

def get_vacancies(specialization_ids):
    links = []
    for specialization_id in specialization_ids:
        page = requests.get('https://api.hh.ru/vacancies?specialization={}'.format(specialization_id)).json()
        pages = page['pages']
        per_page = page['per_page']

        for i in tqdm(range(pages), 'Загрузка списка ссылок на вакансии для ' + str(specialization_id)):
            r = requests.get('https://api.hh.ru/vacancies?specialization={}'.format(specialization_id), params={'page': i, 'per_page': per_page}).json()
            for j in r['items']:
                links.append(j['url'])
    
    return [requests.get(i).json() for i in tqdm(links, 'Загрузка вакансий')]

def get_requirements(vacs):
    regex_start = ''
    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/vacabulary_start.csv') as f_in:
        for line in f_in:
            regex_start += line.replace('\n', '') + '|'

    regex_end = ''
    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/vacabulary_end.csv') as f_in:
        for line in f_in:
            regex_end += line.replace('\n', '') + '|'

    regex = re.compile('(?:' + regex_start[:-1] + ')' + '.*?' + '(?:' + regex_end[:-1] + ')')

    desc = [i['description'] for i in tqdm(vacs, 'Сбор описания требуемых навыков')]

    reqs_text = []
    for i in desc:
        reqs_text += regex.findall(i, re.IGNORECASE)

    reqs = []
    for i in reqs_text:
        for j in re.findall(r'<li>.*?<\/li>', i):
            reqs.append(re.sub(r'^ +', '', re.sub(r'<.*?>', '', str(j))).capitalize())

    return {k: v for k, v in sorted(Counter(reqs).items(), key=lambda item: item[1], reverse=True)}

def get_key_skills(vacs):
    skills = []
    for i in tqdm(vacs, 'Сбор требуемых навыков'):
        for j in i['key_skills']:
            skills.append(j['name'])
    
    return {k: v for k, v in sorted(Counter(skills).items(), key=lambda item: item[1], reverse=True)}

def to_csv(dict_data, file_name):
    with open(os.path.dirname(os.path.abspath(__file__)) + '/data/' + file_name + '.csv', 'w') as f_out:
        f_out.write('Number;Required skill;Number of repetitions\n')
        for i in tqdm(range(len(dict_data.keys())), 'Вывод в файл ' + str(file_name)):
            f_out.write(str(i) + ';\"' + str(list(dict_data.keys())[i]) + '\";' + str(list(dict_data.values())[i]) + '\n')
        f_out.close()

if __name__ == "__main__":
    pass