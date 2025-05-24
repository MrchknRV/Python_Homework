import re
from collections import Counter


def filter_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению."""
    return [item for item in dict_list if item.get("state") == state]


def sort_by_date(dict_list: list, reverse: bool = True) -> list:
    """Функция должна возвращает новый список, отсортированный по дате"""
    return sorted(dict_list, key=lambda x: x.get("date"), reverse=reverse)


def search_banking_transactions_by_string(transactions: list, search_string=None) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    try:
        if search_string is None:
            return transactions
        pattern = f"{search_string}?"
        if len(transactions) > 0:
            result = []
            for trans in transactions:
                if re.search(pattern, trans.get("description", ""), re.IGNORECASE) is not None:
                    result.append(trans)
            return result
        return []
    except Exception:
        return []


def get_count_transactions_category(transactions: list, list_categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    try:
        if len(list_categories) == 0:
            return {}

        if len(transactions) > 0:
            result_list = []
            for category in list_categories:
                pattern = f"{category}?"
                for trans in transactions:
                    result = re.findall(pattern, trans.get("description", ""), re.IGNORECASE)
                    result_list = result_list + result
                    print(result_list)

            result_dict = Counter(result_list)
            return result_dict
        return {}
    except Exception:
        return {}
