from workshop_system.config import ITEMS_LIST_RESPONSE, PAGE_QUERY_PARAM, PAGE_SIZE_QUERY_PARAM


def get_list_response_dict(page: int, page_size: int, items: [dict]):
    return {
        PAGE_QUERY_PARAM: page,
        PAGE_SIZE_QUERY_PARAM: page_size,
        ITEMS_LIST_RESPONSE: items
    }
