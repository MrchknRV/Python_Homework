from src.generators import filter_by_currency, transaction_description


def test_filter_by_currency_empty() -> None:
    assert filter_by_currency([]) == "Нет данных"


def test_filter_by_currency_mistake_code(sample_currency: list) -> None:
    assert filter_by_currency(sample_currency, "AAA") == "Неверно указан код валюты"
    assert filter_by_currency(sample_currency, "DS1") == "Неверно указан код валюты"
    assert filter_by_currency(sample_currency, "DSd1") == "Неверно указан код валюты"


def test_filter_by_currency_default(sample_currency: list) -> None:
    current_result = filter_by_currency(sample_currency)
    assert next(current_result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(current_result) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(current_result) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Platinum 9276828925530562",
        "to": "Maestro 3806652527413662",
    }


def test_filter_by_currency_RUB(sample_currency: list) -> None:
    current_result = filter_by_currency(sample_currency, "RUB")
    assert next(current_result) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(current_result) == {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {"amount": "30153.72", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655",
    }
    assert next(current_result) == {
        "id": 596171168,
        "state": "EXECUTED",
        "date": "2018-07-11T02:26:18.671407",
        "operationAmount": {"amount": "79931.03", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 72082042523231456215",
    }
    assert next(current_result) == {
        "id": 147815167,
        "state": "EXECUTED",
        "date": "2018-01-26T15:40:13.413061",
        "operationAmount": {"amount": "50870.71", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 4598300720424501",
        "to": "Счет 43597928997568165086",
    }
    assert next(current_result) == {
        "id": 615064591,
        "state": "CANCELED",
        "date": "2018-10-14T08:21:33.419441",
        "operationAmount": {"amount": "77751.04", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод с карты на счет",
        "from": "Maestro 3928549031574026",
        "to": "Счет 84163357546688983493",
    }


def test_filter_by_currency_EUR(sample_currency: list) -> None:
    current_result = filter_by_currency(sample_currency, "EUR")
    assert next(current_result) == {
        "id": 214024827,
        "state": "CANCELED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {"amount": "70946.18", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366",
    }
    assert next(current_result) == {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "EUR", "code": "EUR"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_filter_by_currency_missing_currency(sample_currency_missing_currency: list) -> None:
    current_result = filter_by_currency(sample_currency_missing_currency, "USD")
    current_result_RUB = filter_by_currency(sample_currency_missing_currency, "RUB")
    assert next(current_result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(current_result_RUB) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(current_result_RUB) == {
        "id": 522357576,
        "state": "EXECUTED",
        "date": "2019-11-19T09:22:25.899614",
        "operationAmount": {"amount": "30153.72", "currency": {"name": "RUB", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655",
    }


def test_transaction_description(sample_transaction: list) -> None:
    current_result = transaction_description(sample_transaction)
    assert next(current_result) == "Перевод организации"
    assert next(current_result) == "Перевод со счета на счет"
    assert next(current_result) == "Перевод со счета на счет"
    assert next(current_result) == "Перевод организации"


def test_transaction_description_missing_description(sample_transaction_missing_description: list) -> None:
    current_result = transaction_description(sample_transaction_missing_description)
    assert next(current_result) == "Информация отсутствует"
    assert next(current_result) == "Перевод со счета на счет"
    assert next(current_result) == "Информация отсутствует"
    assert next(current_result) == "Перевод организации"
    assert next(current_result) == "Перевод организации"


def test_transaction_description_empty() -> None:
    current_result = transaction_description([])
    assert next(current_result) == "Нет данных"
