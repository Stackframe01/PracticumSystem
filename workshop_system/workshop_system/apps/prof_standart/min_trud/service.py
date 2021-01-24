from datetime import date, timedelta
from typing import Optional

import schedule

from workshop_system.apps.prof_standart.min_trud.client import ProfStandartClient
from workshop_system.apps.prof_standart.min_trud.dto import GeneralizedWorkFunction, ProfStandart
from workshop_system.apps.prof_standart.min_trud.model import JobTitle, ProfessionalStandart


class ProfStandartService:
    _prof_standart_client: ProfStandartClient = ProfStandartClient()

    _prof_standart_relevance_days: int = 180

    def __init__(self):
        schedule \
            .every(self._prof_standart_relevance_days) \
            .days.at("05:00") \
            .do(self._remove_old_prof_standarts)

    @classmethod
    def _remove_old_prof_standarts(cls) -> None:
        time_threshold: date = date.today() - timedelta(days=cls._prof_standart_relevance_days)
        ProfessionalStandart.objects.filter(created__lt=time_threshold)

    @classmethod
    def _get_job_title(cls, job_titles, pjt):
        if pjt not in [jt.name for jt in job_titles]:
            job_title: JobTitle = JobTitle(name=pjt)
            job_title.save()
            job_titles.append(job_title)

    @classmethod
    def _get_and_save_professional_standart(cls, prof_standart: ProfStandart, found_by: str) -> ProfessionalStandart:
        try:
            found_professional_standart: ProfessionalStandart = ProfessionalStandart.objects \
                .filter(code=prof_standart.first_section.code_kind_professional_activity) \
                .get()
        except ProfessionalStandart.DoesNotExist:
            professional_standart: ProfessionalStandart = ProfessionalStandart(
                code=prof_standart.first_section.code_kind_professional_activity,
                name=prof_standart.name_professional_standart,
                found_by=found_by
            )
            professional_standart.save()

            job_titles: [JobTitle] = []
            for gwf in prof_standart.third_section.work_functions.generalized_work_functions.generalized_work_function:
                if isinstance(gwf, GeneralizedWorkFunction) and gwf.possible_job_titles:
                    if isinstance(gwf.possible_job_titles.possible_job_title, list):
                        for pjt in gwf.possible_job_titles.possible_job_title:
                            cls._get_job_title(job_titles, pjt)
                    else:
                        pjt: str = gwf.possible_job_titles.possible_job_title
                        cls._get_job_title(job_titles, pjt)
            if job_titles:
                professional_standart.job_titles.set(job_titles)

            return professional_standart

        setattr(found_professional_standart, 'found_by', found_by)
        found_professional_standart.save()
        return found_professional_standart

    @classmethod
    def _get_and_save_prof_standart_by_code_from_client(cls, code: str) -> Optional[ProfessionalStandart]:
        try:
            prof_standart: ProfStandart = cls._prof_standart_client.find_prof_standart_by_code(code)
        except ProfStandart.WasNotFound:
            return None

        professional_standart = cls._get_and_save_professional_standart(prof_standart, code)

        return professional_standart

    @classmethod
    def _get_and_save_prof_standarts_by_name_from_client(cls, name: str) -> [ProfessionalStandart]:
        try:
            prof_standart_list: [ProfStandart] = cls._prof_standart_client.find_prof_standarts_by_name(name)
        except ProfStandart.WasNotFound:
            return []

        professional_standart_list: [ProfessionalStandart] = []
        for prof_standart in prof_standart_list:
            professional_standart = cls._get_and_save_professional_standart(prof_standart, name)
            professional_standart_list.append(professional_standart)

        return professional_standart_list

    @classmethod
    def _get_or_save_prof_standart_by_code(cls, code: str) -> Optional[ProfessionalStandart]:
        professional_standart: ProfessionalStandart = ProfessionalStandart.objects \
            .filter(code=code) \
            .order_by('created') \
            .last()

        if not professional_standart:
            return cls._get_and_save_prof_standart_by_code_from_client(code)

        return professional_standart

    @classmethod
    def _get_or_save_prof_standart_by_name(cls, name: str, start: int, end: int) -> [ProfessionalStandart]:
        prof_standart_list: [ProfessionalStandart] = \
            ProfessionalStandart.objects.filter(found_by=name).all()
        if not prof_standart_list:
            prof_standart_list = \
                cls._get_and_save_prof_standarts_by_name_from_client(name)

        prof_standart_list_len = len(prof_standart_list)
        if prof_standart_list_len >= end:
            return prof_standart_list[start: end]
        if prof_standart_list_len > start:
            return prof_standart_list[start:]
        return []

    @classmethod
    def find_prof_standart_by_code(cls, code: str) -> ProfessionalStandart:
        professional_standart: ProfessionalStandart = cls._get_or_save_prof_standart_by_code(code)

        if not professional_standart:
            raise ProfessionalStandart.DoesNotExist

        return professional_standart

    @classmethod
    def find_prof_standart_by_name(cls, page: int, page_size: int, name: str):
        return cls._get_or_save_prof_standart_by_name(name, page * page_size, (page + 1) * page_size)
