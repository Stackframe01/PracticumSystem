from django.urls import include, path

from workshop_system.apps.labor_market.hh_ru import urls as hh_ru_urls

urlpatterns = [
    path('hh-ru/', include(hh_ru_urls)),
]
