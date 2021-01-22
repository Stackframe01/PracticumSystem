from django.urls import re_path

from workshop_system.apps.labor_market.hh_ru import view
from workshop_system.apps.labor_market.hh_ru.config import VACANCY_CODE_PARAM_PATH_PARAM

urlpatterns = [
    re_path(r'^vacancies/?', view.VacancyListAPIView.as_view()),
    re_path(f'^vacancies/{VACANCY_CODE_PARAM_PATH_PARAM}/?', view.VacancyAPIView.as_view()),
]
