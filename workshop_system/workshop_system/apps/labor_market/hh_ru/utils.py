from rest_framework.request import Request

from workshop_system.apps.labor_market.hh_ru.config import DEFAULT_PAGE_SIZE, KEY_WORDS_QUERY_PARAM, MAX_PAGE_SIZE, \
    PAGE_QUERY_PARAM, PAGE_SIZE_QUERY_PARAM, VACANCY_CODE_PATH_PARAM


def get_vacancy_code(**kwargs: {str}) -> int:
    try:
        return int(kwargs[VACANCY_CODE_PATH_PARAM])
    except KeyError or TypeError:
        return -1


def get_key_words(request: Request) -> str:
    try:
        return request.query_params.get(KEY_WORDS_QUERY_PARAM)
    except KeyError:
        return ''


def get_page(request: Request) -> int:
    try:
        page: int = int(request.query_params.get(PAGE_QUERY_PARAM))
    except TypeError:
        return 0

    if page:
        if page < 0:
            page = 0
    else:
        page = 0

    return page


def get_page_size(request: Request) -> int:
    try:
        page_size: int = int(request.query_params.get(PAGE_SIZE_QUERY_PARAM))
    except TypeError:
        return DEFAULT_PAGE_SIZE

    if page_size:
        if page_size <= 0:
            page_size = DEFAULT_PAGE_SIZE

        if page_size > MAX_PAGE_SIZE:
            page_size = MAX_PAGE_SIZE
    else:
        page_size = DEFAULT_PAGE_SIZE

    return page_size
