VACANCY_CODE_PATH_PARAM: str = 'vacancy_code'
VACANCY_CODE_PARAM_PATH_PARAM: str = rf'(?P<{VACANCY_CODE_PATH_PARAM}>\d{0,25})'

KEY_WORDS_QUERY_PARAM: str = 'key_words'
PAGE_QUERY_PARAM: str = 'page'
PAGE_SIZE_QUERY_PARAM: str = 'page_size'
ITEMS_LIST_RESPONSE: str = 'items'

DEFAULT_PAGE_SIZE: int = 10
MAX_PAGE_SIZE: int = 100

ERROR_MESSAGE: str = 'error'
VACANCY_REQUEST_ERROR: dict = {ERROR_MESSAGE: 'vacancy retrieve internal error'}
VACANCY_NOT_FOUND_ERROR: dict = {ERROR_MESSAGE: 'vacancy with specified code was not found'}
