from workshop_system.utls import get_error_dict

VACANCY_CODE_PATH_PARAM: str = 'vacancy_code'
VACANCY_CODE_PATH_PARAM_MATCH: str = f'<int:{VACANCY_CODE_PATH_PARAM}>'

KEY_WORDS_QUERY_PARAM: str = 'key_words'

VACANCY_REQUEST_ERROR: dict = get_error_dict('vacancy retrieve internal error')
VACANCY_NOT_FOUND_ERROR: dict = get_error_dict('vacancy with specified code was not found')
