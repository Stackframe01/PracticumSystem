from rest_framework.request import Request

from workshop_system.config import DEFAULT_PAGE_SIZE, ERROR_MESSAGE, MAX_PAGE_SIZE, PAGE_QUERY_PARAM, \
    PAGE_SIZE_QUERY_PARAM


def get_error_dict(message: str):
    return {ERROR_MESSAGE: message}


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


def get_int_path_param(param_name: str, **kwargs: {str}) -> int:
    try:
        return int(kwargs[param_name])
    except KeyError or TypeError:
        return -1


def get_str_path_param(param_name: str, **kwargs: {str}) -> str:
    try:
        return kwargs[param_name]
    except KeyError:
        return ''


def get_str_query_param(param_name: str, request: Request) -> str:
    query_param: str = request.query_params.get(param_name)

    if not query_param:
        return ''

    return query_param
