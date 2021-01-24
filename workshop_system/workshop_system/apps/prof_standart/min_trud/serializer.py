from workshop_system.apps.prof_standart.min_trud.model import ProfessionalStandart
from workshop_system.serializer import get_list_response_dict


def prof_standart_to_dict(prof_standart: ProfessionalStandart) -> dict:
    return {
        'code': prof_standart.code,
        'name': prof_standart.name,
        'job_titles': [jt.name for jt in prof_standart.job_titles.all()]
    }


def prof_standart_list_to_dict(page: int, page_size: int, prof_standart_list: [ProfessionalStandart]) -> dict:
    return get_list_response_dict(page, page_size, [prof_standart_to_dict(v) for v in prof_standart_list])
