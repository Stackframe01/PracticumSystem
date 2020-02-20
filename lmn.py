import os
import re
import requests
from tqdm import tqdm

def get_vacancies(search_words):
    search_request = ''
    for i in search_words:
        search_request += i + '+'
    search_request = search_request[:-1]

    page = requests.get('https://api.hh.ru/vacancies?text={}'.format(search_request)).json()
    pages = page['pages']
    per_page = page['per_page']

    ids = []
    for i in tqdm(range(pages), 'Загрузка списка вакансий'):
        r = requests.get('https://api.hh.ru/vacancies?text={}'.format(search_request), params={'page': i, 'per_page': per_page}).json()
        for j in r['items']:
            ids.append(j['id'])
    
    return [requests.get('https://api.hh.ru/vacancies/{}'.format(id)).json() for id in tqdm(ids, 'Загрузка вакансий')]

def get_requirements(vacs):
    regex_start = ''
    with open('data/vocabularies/description_regex_start.csv') as f_in:
        for line in f_in:
            regex_start += '{}|'.format(line.rstrip())

    regex_end = ''
    with open('data/vocabularies/description_regex_end.csv') as f_in:
        for line in f_in:
            regex_end += '{}|'.format(line.rstrip())

    reqs = []
    for i in vacs:
        for j in re.findall('(?:{}).*?(?:{})'.format(regex_start[:-1], regex_end[:-1]), i['description'], re.IGNORECASE):
            for k in re.findall(r'<li>.*?<\/li>', j):
                reqs.append(re.sub(r'(?:^\s+|\.|;|,)', '', re.sub(r'<.*?>', '', str(k))).lower())

    return [i for i in reqs if i != '']

def get_key_skills(vacs):
    skills = []
    for i in vacs:
        for j in i['key_skills']:
            skills.append(j['name'])
    
    for i in skills:
        sequence = re.findall(r'.*?(?:\.|;|,)', i)
        if sequence:
            skills.remove(i)
            skills.extend(sequence)
    
    return [i for i in [re.sub(r'(?:^\s+|\.|;|,)', '', i).lower() for i in skills] if i != '']

if __name__ == "__main__":
    pass