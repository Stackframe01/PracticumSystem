import logging

import requests

from workshop_system.apps.market_needs.clients.hh_ru.models import Vacancy, VacancyList

log = logging.getLogger(__name__)


class RequestError(Exception):
    def __init__(self, code: int = None, message: str = None) -> None:
        Exception.__init__(self, f'Request error, code: {code}, message: {message}')


class HhruApiClient:
    _base_url = 'https://api.hh.ru'
    _vacancies_url = 'vacancies'
    _search_query_param = 'text'
    _page_query_param = 'page'
    _page_size_query_param = 'per_page'

    def find_vacancies_by_key_words(self, key_words: [str], page: int, page_size: int) -> VacancyList:
        url = f'{self._base_url}/{self._vacancies_url}'
        params = {
            self._search_query_param: key_words,
            self._page_query_param: page,
            self._page_size_query_param: page_size
        }
        response = requests.get(url=url, params=params)

        if response.status_code != 200:
            log.error(f'Cannot find vacancies with key words: {key_words}, page: {page}, page_size: {page_size}')
            raise RequestError(response.status_code, response.text)

        result = response.json()
        vacancies = VacancyList.from_dict(result)
        return vacancies

    def find_all_vacancies_by_key_words(self, key_words: [str]) -> [Vacancy]:
        vacancies = [Vacancy]

        page = 1
        page_size = 50
        result = self.find_vacancies_by_key_words(key_words=key_words, page=page, page_size=page_size)

        while result.page < result.pages:
            page += 1
            result = self.find_vacancies_by_key_words(key_words=key_words, page=page, page_size=page_size)
            vacancies.append(result.items)

        return vacancies

    def get_vacancy_by_id(self, vacancy_id: str) -> Vacancy:
        url = f'{self._base_url}/{self._vacancies_url}/{vacancy_id}'
        response = requests.get(url=url)

        if response.status_code != 200:
            log.error(f'Cannot get vacancy with id: {vacancy_id}')
            raise RequestError(response.status_code, response.text)

        vacancy_json = response.json()
        vacancy = Vacancy.from_dict(vacancy_json)
        return vacancy
