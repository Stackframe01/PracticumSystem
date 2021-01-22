from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request

from workshop_system.apps.labor_market.hh_ru.client import RequestError
from workshop_system.apps.labor_market.hh_ru.config import VACANCY_NOT_FOUND_ERROR, VACANCY_REQUEST_ERROR
from workshop_system.apps.labor_market.hh_ru.model import Vacancy
from workshop_system.apps.labor_market.hh_ru.serializer import vacancy_list_to_dict, vacancy_to_dict
from workshop_system.apps.labor_market.hh_ru.service import HhRuService
from workshop_system.apps.labor_market.hh_ru.utils import get_key_words, get_page, get_page_size, get_vacancy_code


class VacancyAPIView(RetrieveAPIView):
    _hh_ru_service: HhRuService = HhRuService()

    def get(self, request: Request, *args: [str], **kwargs: {str}):
        print(kwargs)
        vacancy_code: int = get_vacancy_code(**kwargs)

        try:
            vacancy: Vacancy = self._hh_ru_service.get_vacancy(vacancy_code)
        except RequestError:
            return JsonResponse(data=VACANCY_REQUEST_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Vacancy.DoesNotExist:
            return JsonResponse(data=VACANCY_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)

        vacancy_dict: dict = vacancy_to_dict(vacancy)

        return JsonResponse(data=vacancy_dict, status=status.HTTP_200_OK)


class VacancyListAPIView(ListAPIView):
    _hh_ru_service: HhRuService = HhRuService()

    def get(self, request: Request, *args: [str], **kwargs: [str]):
        page: int = get_page(request)
        page_size: int = get_page_size(request)
        key_words: str = get_key_words(request)

        try:
            vacancy_list: [Vacancy] = self._hh_ru_service.find_vacancies(key_words, page, page_size)
        except RequestError:
            return JsonResponse(data=VACANCY_REQUEST_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        list_response: dict = vacancy_list_to_dict(page, page_size, vacancy_list)

        return JsonResponse(data=list_response, status=status.HTTP_200_OK)
