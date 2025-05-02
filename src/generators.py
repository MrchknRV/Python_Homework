from typing import Any, Generator

LIST_CODE = [
    "USD",
    "EUR",
    "GBP",
    "JPY",
    "CNY",
    "AUD",
    "CAD",
    "CHF",
    "SEK",
    "NOK",
    "DKK",
    "NZD",
    "SGD",
    "HKD",
    "KRW",
    "INR",
    "BRL",
    "MXN",
    "ZAR",
    "RUB",
    "TRY",
    "AED",
    "SAR",
    "PLN",
    "THB",
    "IDR",
    "MYR",
    "PHP",
    "VND",
    "KZT",
    "UAH",
    "BYN",
    "KWD",
    "QAR",
    "CLP",
    "COP",
    "PEN",
    "ARS",
    "ILS",
    "EGP",
    "NGN",
    "XDR",
    "XAU",
    "XAG",
    "BTC",
    "ETH",
]


def filter_by_currency(transactions: list[dict], currency: str = "USD") -> Any:
    """Функция, которая принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной
    (по умолчанию, USD)."""
    valid_transactions = []
    for transaction in transactions:
        if (
            transaction["operationAmount"].get("currency", 0)
            and transaction["operationAmount"]["currency"].get("code", 0) != 0
        ):
            valid_transactions.append(transaction)
    if currency not in LIST_CODE or len(currency) > 4 and not currency.isalpha():
        return "Неверно указан код валюты"
    elif len(valid_transactions) > 0:
        return iter(filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, valid_transactions))
    return "Нет данных"


def transaction_description(transactions: list[dict]) -> Generator:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    if len(transactions) > 0:
        for transaction in transactions:
            if transaction.get("description") is None:
                yield "Информация отсутствует"
            else:
                yield transaction.get("description")
    yield "Нет данных"


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров"""
    for num in range(abs(int(start)), abs(int(stop)) + 1):
        card_num = f"{num:016d}"
        formatted_num = " ".join([card_num[i: i + 4] for i in range(0, 16, 4)])
        yield formatted_num
