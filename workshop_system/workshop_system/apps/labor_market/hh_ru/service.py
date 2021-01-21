from datetime import date, timedelta

import schedule

from workshop_system.apps.labor_market.hh_ru.client import HhRuApiClient
from workshop_system.apps.labor_market.hh_ru.dto import VacancyItem, VacancyList, VacancyFull
from workshop_system.apps.labor_market.hh_ru.model import Vacancy, KeySkill


class HhRuService:
    _vacancy_relevance_days = 30
    _hh_ru_api_client: HhRuApiClient = HhRuApiClient()

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
    def _get_vacancy_from_api(cls, code) -> Vacancy:
        vacancy: VacancyFull = cls._hh_ru_api_client.get_vacancy_by_id(vacancy_id=code)
        key_skills: [KeySkill] = [KeySkill(ks.name) for ks in vacancy.key_skills]
        vacancy: Vacancy = Vacancy(
            code=vacancy.id,
            name=vacancy.name,
            key_skills=key_skills,
            description_skills=vacancy.description
        )
        return vacancy

    @classmethod
    def _get_or_save_vacancy_list(cls, codes: [int]) -> [Vacancy]:
        vacancy_list: [Vacancy] = Vacancy.objects.get(code=codes)
        not_saved_codes: [int] = [vd for vd in vacancy_list if vd.id not in codes]

        for code in not_saved_codes:
            vacancy: Vacancy = cls._get_vacancy_from_api(code)
            vacancy.save()
            vacancy_list.append(vacancy)

        return vacancy_list

    @classmethod
    def _get_vacancy_list(cls, key_words, page, page_size) -> VacancyList:
        vacancy_item_list: VacancyList = cls._hh_ru_api_client.find_vacancies(
            key_words=key_words,
            page=page,
            page_size=page_size
        )
        return vacancy_item_list

    @classmethod
    def _get_all_vacancy_list(cls, key_words: [str]) -> [Vacancy]:
        page: int = 1
        page_size: int = 50
        vacancy_item_list: VacancyList = cls._get_vacancy_list(key_words, page, page_size)
        all_vacancy_item_list: [VacancyItem] = vacancy_item_list.items

        while vacancy_item_list.page < vacancy_item_list.pages:
            page += 1
            vacancy_item_list: VacancyList = cls._get_vacancy_list(key_words, page, page_size)
            all_vacancy_item_list.extend(vacancy_item_list.items)

        codes: [int] = [vi.id for vi in all_vacancy_item_list]
        all_vacancy_list: [Vacancy] = cls._get_or_save_vacancy_list(codes)

        return all_vacancy_list

    @classmethod
    def find_vacancies(cls, key_words: [str]) -> [Vacancy]:
        return cls._get_all_vacancy_list(key_words)
