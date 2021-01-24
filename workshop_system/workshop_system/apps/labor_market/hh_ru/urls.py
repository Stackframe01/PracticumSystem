from django.urls import path, re_path

from workshop_system.apps.labor_market.hh_ru.config import VACANCY_CODE_PATH_PARAM_MATCH
from workshop_system.apps.labor_market.hh_ru.view import VacancyAPIView, VacancyListAPIView

urlpatterns = [
    path(f'vacancies/{VACANCY_CODE_PATH_PARAM_MATCH}', VacancyAPIView.as_view()),
    re_path(r'^vacancies/?', VacancyListAPIView.as_view()),
]
