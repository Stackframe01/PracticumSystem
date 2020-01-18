import os
import re
import requests
from tqdm import tqdm

def get_specializations():
    spec = requests.get('https://api.hh.ru/specializations').json()

    regex = ''
    with open('data/vocabularies/specializations_regex.csv') as f_in:
        for line in f_in:
            regex += '{}|'.format(line.rstrip())

    ids = []
    for i in spec:
        for j in i["specializations"]:
            if re.search('(?:{})'.format(regex[:-1]), j['name'], re.IGNORECASE):
                ids.append(j['id'])
    
    return ids

def get_vacancies(specializations_ids):
    ids = []

    for specialization_id in specializations_ids:
        page = requests.get('https://api.hh.ru/vacancies?specialization={}'.format(specialization_id)).json()
        pages = 5 # page['pages']
        per_page = page['per_page']

        for i in tqdm(range(pages), 'Загрузка списка вакансий для {}'.format(specialization_id)):
            r = requests.get('https://api.hh.ru/vacancies?specialization={}'.format(specialization_id), params={'page': i, 'per_page': per_page}).json()
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

    regex = re.compile('(?:{}).*?(?:{})'.format(regex_start[:-1], regex_end[:-1]))

    desc = [i['description'] for i in vacs]

    reqs_text = []
    for i in desc:
        reqs_text += regex.findall(i, re.IGNORECASE)

    reqs = []
    for i in reqs_text:
        for j in re.findall(r'<li>.*?<\/li>', i):
            reqs.append(re.sub(r'(?:^ +|\.|;|,)', '', re.sub(r'<.*?>', '', str(j))).lower())

    return reqs

def get_key_skills(vacs):
    skills = []
    for i in vacs:
        for j in i['key_skills']:
            skills.append(str(j['name']).lower())
    
    for i in range(len(skills)):
        if re.findall(r'.*?(?:\.|;|,|")', skills[i]):
            for j in re.findall(r'.*?(?:\.|;|,|")', skills[i]):
                if re.sub(r'(?:^ +|\.|;|,)', '', j) != '':
                    skills.append(re.sub(r'(?:^ +|\.|;|,)', '', j))
            del skills[i]

    return skills

def to_csv(file_name, data):
    with open('data/{}.csv'.format(file_name), 'w') as f_out:
        f_out.write(';Required skill\n')
        for i in range(len(data)):
            f_out.write('{};{}\n'.format(i, data[i]))
        f_out.close()

if __name__ == "__main__":
    pass