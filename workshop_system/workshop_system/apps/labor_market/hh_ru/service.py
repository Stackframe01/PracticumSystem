import math
from datetime import date, timedelta
from typing import Optional

import schedule

from workshop_system.apps.labor_market.hh_ru.client import HhRuApiClient
from workshop_system.apps.labor_market.hh_ru.dto import VacancyFull, VacancyItem, VacancyList
from workshop_system.apps.labor_market.hh_ru.model import KeySkill, Vacancy


class HhRuService:
    _hh_ru_api_client: HhRuApiClient = HhRuApiClient()

    _page_size: int = 50
    _vacancy_relevance_days: int = 30

    def __init__(self):
        schedule \
            .every(self._vacancy_relevance_days) \
            .days.at("05:00") \
            .do(self._remove_old_vacancies)

    @classmethod
    def _remove_old_vacancies(cls) -> None:
        time_threshold: date = date.today() - timedelta(days=cls._vacancy_relevance_days)
        Vacancy.objects.filter(created__lt=time_threshold)

    @classmethod
    def _get_and_save_vacancy_from_client(cls, code: int) -> Optional[Vacancy]:
        try:
            vacancy_full: VacancyFull = cls._hh_ru_api_client.get_vacancy_by_id(vacancy_id=code)
        except VacancyFull.WasNotFound:
            return None

        vacancy: Vacancy = Vacancy(
            code=vacancy_full.id,
            name=vacancy_full.name,
            description=vacancy_full.description
        )
        vacancy.save()

        key_skills: [KeySkill] = []
        for ks in vacancy_full.key_skills:
            key_skill: KeySkill = KeySkill(name=ks.name)
            key_skill.save()
            key_skills.append(key_skill)
        if key_skills:
            vacancy.key_skills.set(key_skills)

        return vacancy

    @classmethod
    def _get_or_save_vacancy_list(cls, codes: [int]) -> [Vacancy]:
        vacancy_list: [Vacancy] = list(Vacancy.objects.filter(code__in=codes))

        vacancy_id_list: [int] = [v.code for v in vacancy_list]
        not_saved_codes: [int] = [c for c in codes if c not in vacancy_id_list]

        for code in not_saved_codes:
            vacancy: Vacancy = cls._get_and_save_vacancy_from_client(code)

            if vacancy:
                vacancy_list.append(vacancy)

        return vacancy_list

    @classmethod
    def _find_vacancy_list_from_client(cls, key_words: str, page: int, page_size: int) -> VacancyList:
        vacancy_item_list: VacancyList = cls._hh_ru_api_client.find_vacancies(
            key_words=key_words,
            page=page,
            page_size=page_size
        )
        return vacancy_item_list

    @classmethod
    def get_vacancy(cls, code: int) -> Vacancy:
        vacancy_list: [Vacancy] = cls._get_or_save_vacancy_list([code])

        if not vacancy_list:
            raise Vacancy.DoesNotExist

        return vacancy_list[0]

    @classmethod
    def find_vacancies(cls, key_words: str, page: int, page_size: int) -> [Vacancy]:
        pages: int = math.ceil(page_size / cls._page_size)

        all_vacancy_item_list: [VacancyItem] = []
        for p in range(pages):
            vacancy_item_list: VacancyList = cls._find_vacancy_list_from_client(key_words, page + p, cls._page_size)
            all_vacancy_item_list.extend(vacancy_item_list.items)

        codes: [int] = [vi.id for vi in all_vacancy_item_list]
        all_vacancy_list: [Vacancy] = cls._get_or_save_vacancy_list(codes)

        return all_vacancy_list

    @classmethod
    def find_all_vacancies(cls, key_words: str) -> [Vacancy]:
        page: int = 1
        vacancy_item_list: VacancyList = cls._find_vacancy_list_from_client(key_words, page, cls._page_size)
        all_vacancy_item_list: [VacancyItem] = vacancy_item_list.items

        while vacancy_item_list.page < vacancy_item_list.pages:
            page += 1
            vacancy_item_list: VacancyList = cls._find_vacancy_list_from_client(key_words, page, cls._page_size)
            all_vacancy_item_list.extend(vacancy_item_list.items)

        codes: [int] = [vi.id for vi in all_vacancy_item_list]
        all_vacancy_list: [Vacancy] = cls._get_or_save_vacancy_list(codes)

        return all_vacancy_list
