import logging

import requests
from dacite import from_dict

from workshop_system.apps.labor_market.hh_ru.dto import VacancyList, VacancyFull

log = logging.getLogger(__name__)


class RequestError(Exception):
    def __init__(self, code: int = None, message: str = None) -> None:
        Exception.__init__(self, f'Request error, code: {code}, message: {message}')


class HhRuApiClient:
    _base_url = 'https://api.hh.ru'
    _vacancies_url = 'vacancies'
    _search_param = 'text'
    _premium_param = 'premium'
    _page_param = 'page'
    _page_size_param = 'per_page'

    @classmethod
    def find_vacancies(cls, key_words: [str], page: int, page_size: int) -> VacancyList:
        url = f'{cls._base_url}/{cls._vacancies_url}'
        params = {
            cls._search_param: key_words,
            cls._premium_param: True,
            cls._page_param: page,
            cls._page_size_param: page_size
        }
        response = requests.get(url=url, params=params)

        if response.status_code != 200:
            log.error(f'Cannot find vacancies by key words: {key_words}, page: {page}, page_size: {page_size}')
            raise RequestError(response.status_code, response.text)

        vacancy_list_data = response.json()
        vacancy_list = from_dict(data_class=VacancyList, data=vacancy_list_data)

        return vacancy_list

    @classmethod
    def get_vacancy_by_id(cls, vacancy_id: int) -> VacancyFull:
        url = f'{cls._base_url}/{cls._vacancies_url}/{vacancy_id}'
        response = requests.get(url=url)

        if response.status_code != 200:
            log.error(f'Cannot get vacancy with id: {vacancy_id}')
            raise RequestError(response.status_code, response.text)

        vacancy_data = response.json()
        vacancy = from_dict(data_class=VacancyFull, data=vacancy_data)

        return vacancy
