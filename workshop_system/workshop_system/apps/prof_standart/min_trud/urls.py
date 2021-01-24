from django.urls import path, re_path

from workshop_system.apps.prof_standart.min_trud.config import PROF_STANDART_CODE_PATH_PARAM_MATCH
from workshop_system.apps.prof_standart.min_trud.view import ProfStandartAPIView, ProfStandartListAPIView

urlpatterns = [
    path(f'standarts/{PROF_STANDART_CODE_PATH_PARAM_MATCH}', ProfStandartAPIView.as_view()),
    re_path(r'^standarts/?', ProfStandartListAPIView.as_view()),
]
