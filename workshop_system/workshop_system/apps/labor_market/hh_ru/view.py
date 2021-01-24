from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request

from workshop_system.apps.labor_market.hh_ru.client import HhRuRequestError
from workshop_system.apps.labor_market.hh_ru.config import KEY_WORDS_QUERY_PARAM, VACANCY_CODE_PATH_PARAM, \
    VACANCY_NOT_FOUND_ERROR, \
    VACANCY_REQUEST_ERROR
from workshop_system.apps.labor_market.hh_ru.model import Vacancy
from workshop_system.apps.labor_market.hh_ru.serializer import vacancy_list_to_dict, vacancy_to_dict
from workshop_system.apps.labor_market.hh_ru.service import HhRuService
from workshop_system.utls import get_int_path_param, get_page, get_page_size, get_str_query_param


class VacancyAPIView(RetrieveAPIView):
    _hh_ru_service: HhRuService = HhRuService()

    def get(self, request: Request, *args: [str], **kwargs: {str}):
        vacancy_code: int = get_int_path_param(VACANCY_CODE_PATH_PARAM, **kwargs)

        try:
            vacancy: Vacancy = self._hh_ru_service.get_vacancy(vacancy_code)
        except HhRuRequestError:
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
        key_words: str = get_str_query_param(KEY_WORDS_QUERY_PARAM, request)

        try:
            vacancy_list: [Vacancy] = self._hh_ru_service.find_vacancies(key_words, page, page_size)
        except HhRuRequestError:
            return JsonResponse(data=VACANCY_REQUEST_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        vacancy_list_response_dict: dict = vacancy_list_to_dict(page, page_size, vacancy_list)

        return JsonResponse(data=vacancy_list_response_dict, status=status.HTTP_200_OK)
