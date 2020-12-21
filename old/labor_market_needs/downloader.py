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
        r = requests.get('https://api.hh.ru/vacancies?text={}'.format(search_request),
                         params={'page': i, 'per_page': per_page}).json()
        for j in r['items']:
            ids.append(j['id'])

    return [requests.get('https://api.hh.ru/vacancies/{}'.format(id)).json() for id in tqdm(ids, 'Загрузка вакансий')]


if __name__ == '__main__':
    pass
