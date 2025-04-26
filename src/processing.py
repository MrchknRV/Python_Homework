def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    return [item for item in dict_list if item.get("state") == state]


def sort_by_date(dict_list: list, reverse: bool = True) -> list:
    """Функция должна возвращает новый список, отсортированный по дате"""
    return sorted(dict_list, key=lambda x: x.get("date"), reverse=reverse)
