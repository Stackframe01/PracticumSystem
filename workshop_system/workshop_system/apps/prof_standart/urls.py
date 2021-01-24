from django.urls import include, path

from workshop_system.apps.prof_standart.min_trud import urls as min_trud_urls

urlpatterns = [
    path('min-trud/', include(min_trud_urls)),
]
