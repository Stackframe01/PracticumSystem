from django.db import models

from workshop_system.apps.labor_market.hh_ru.config import ITEMS_LIST_RESPONSE, PAGE_QUERY_PARAM, PAGE_SIZE_QUERY_PARAM
from workshop_system.apps.labor_market.hh_ru.model import Vacancy


def vacancy_to_dict(vacancy: Vacancy) -> dict:
    return {
        'code': vacancy.code,
        'name': vacancy.name,
        'description': vacancy.description,
        'key_skills': [ks.name for ks in vacancy.key_skills.all()]
    }


def vacancy_list_to_dict(page: int, page_size: int, vacancy_list: [models.Model]) -> dict:
    return {
        PAGE_QUERY_PARAM: page,
        PAGE_SIZE_QUERY_PARAM: page_size,
        ITEMS_LIST_RESPONSE: [vacancy_to_dict(v) for v in vacancy_list]
    }
