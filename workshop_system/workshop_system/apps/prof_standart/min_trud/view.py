from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.request import Request

from workshop_system.apps.prof_standart.min_trud.client import ProfStandartRequestError
from workshop_system.apps.prof_standart.min_trud.config import PROF_STANDART_CODE_PATH_PARAM, \
    PROF_STANDART_NAME_QUERY_PARAM, \
    PROF_STANDART_NOT_FOUND_ERROR, \
    PROF_STANDART_REQUEST_ERROR
from workshop_system.apps.prof_standart.min_trud.model import ProfessionalStandart
from workshop_system.apps.prof_standart.min_trud.serializer import prof_standart_list_to_dict, prof_standart_to_dict
from workshop_system.apps.prof_standart.min_trud.service import ProfStandartService
from workshop_system.utls import get_page, get_page_size, get_str_path_param, get_str_query_param


class ProfStandartAPIView(RetrieveAPIView):
    _prof_standart_service: ProfStandartService = ProfStandartService()

    def get(self, request: Request, *args: [str], **kwargs: {str}):
        prof_standart_code: str = get_str_path_param(PROF_STANDART_CODE_PATH_PARAM, **kwargs)

        try:
            prof_standart: ProfessionalStandart = \
                self._prof_standart_service.find_prof_standart_by_code(prof_standart_code)
        except ProfStandartRequestError:
            return JsonResponse(data=PROF_STANDART_REQUEST_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except ProfessionalStandart.DoesNotExist:
            return JsonResponse(data=PROF_STANDART_NOT_FOUND_ERROR, status=status.HTTP_404_NOT_FOUND)

        prof_standart_dict: dict = prof_standart_to_dict(prof_standart)

        return JsonResponse(data=prof_standart_dict, status=status.HTTP_200_OK)


class ProfStandartListAPIView(ListAPIView):
    _prof_standart_service: ProfStandartService = ProfStandartService()

    def get(self, request: Request, *args: [str], **kwargs: [str]):
        page: int = get_page(request)
        page_size: int = get_page_size(request)
        prof_standart_name: str = get_str_query_param(PROF_STANDART_NAME_QUERY_PARAM, request)

        try:
            prof_standart_list: [ProfessionalStandart] = \
                self._prof_standart_service.find_prof_standart_by_name(page, page_size, prof_standart_name)
        except ProfStandartRequestError:
            return JsonResponse(data=PROF_STANDART_REQUEST_ERROR, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        vacancy_list_response_dict: dict = prof_standart_list_to_dict(page, page_size, prof_standart_list)

        return JsonResponse(data=vacancy_list_response_dict, status=status.HTTP_200_OK)
