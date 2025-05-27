import json

import pytest

from src.utils import get_financial_transaction_data
from config import PATH

VALID_JSON_DATA = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
]
INVALID_JSON_DATA = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}
INCORRECT_JSON = "{}"


@pytest.fixture
def get_json_file():
    def create_json_file(data=None, filename=PATH / "data" / "test_operation.json"):
        file = filename
        if data is not None:
            with open(filename, "w", encoding="UTF-8") as f:
                f.write(data)
        return str(file)

    return create_json_file


def test_valid_json_file(get_json_file):
    file = get_json_file(data=json.dumps(VALID_JSON_DATA))
    result = get_financial_transaction_data(file)
    assert result == VALID_JSON_DATA


def test_invalid_json_file(get_json_file):
    file = get_json_file(data=json.dumps(INVALID_JSON_DATA))
    result = get_financial_transaction_data(file)
    assert result == []


def test_empty_json_file(get_json_file):
    file = get_json_file(data=json.dumps([]))
    result = get_financial_transaction_data(file)
    assert result == []


def test_incorrect_json_file(get_json_file):
    file = get_json_file(data=json.dumps(INCORRECT_JSON))
    result = get_financial_transaction_data(file)
    assert result == []


def test_not_found_file() -> None:
    result = get_financial_transaction_data("not_found.json")
    assert result == []
