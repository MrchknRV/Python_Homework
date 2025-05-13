import json
import os

BASIC_JSON_FILE_DIR = os.path.abspath(r"..\data\operations.json")


def get_financial_transaction_data(file_dir: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        with open(file_dir, "r", encoding="UTF-8") as json_file:
            json_data = json.load(json_file)
            if not isinstance(json_data, list):
                return []
            return json_data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
