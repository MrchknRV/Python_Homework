import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def transaction_amount(transaction: dict) -> Any:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли"""
    try:
        if transaction["operationAmount"]["currency"]["code"] in ("USD", "EUR"):
            from_ = transaction["operationAmount"]["currency"]["code"]
            to = "RUB"
            amount = transaction["operationAmount"].get("amount")
            headers = {"apikey": API_KEY}
            url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
            response = requests.get(url, headers=headers)
            status_code = response.status_code
            if status_code == 200:
                result = response.json()
                return float(result.get("result"))
            else:
                return f"Не успешный запрос.\nКод ошибки: {status_code} - {response.json()['error'].get('code')}."
        return float(transaction["operationAmount"].get("amount"))
    except KeyError:
        print("Key not found")
