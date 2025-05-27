import csv
import logging

import pandas as pd

from config import PATH

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(PATH / "logs" / "csv_xlsx_reader.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

BASIC_DATA_FILE_CSV = "../data/transactions.csv"
BASIC_DATA_FILE_XLSX = "../data/transactions_excel.xlsx"


def reader_file_transactions_csv(pathfile: str) -> list:
    """Функция для считывания финансовых операций из CSV принимает путь к файлу CSV в качестве аргумента.
    И выдает список словарей с транзакциями."""
    logger.info("Запуск функции %s", reader_file_transactions_csv.__name__)
    try:
        logger.info("Считываем данные из файла %s", pathfile)
        with open(pathfile, encoding="UTF-8") as csvfile:
            reader_csv = csv.DictReader(csvfile, delimiter=";")
            result = list(reader_csv)
            logger.info("Функция %s успешно завершилась", reader_file_transactions_csv.__name__)
            return result
    except (FileNotFoundError, Exception) as ex:
        logger.error("Произошла ошибка %s", ex)
        return []


def reader_file_transactions_xlxs(pathfile: str) -> list:
    """Функция для считывания финансовых операций из Excel принимает путь к файлу Excel в качестве аргумента.
    И выдает список словарей с транзакциями."""
    logger.info("Запуск функции %s", reader_file_transactions_xlxs.__name__)
    try:
        logger.info("Считываем данные из файла %s", pathfile)
        df_excel = pd.read_excel(pathfile, dtype=str, engine="openpyxl")
        transactions = df_excel.to_dict(orient="records")
        logger.info("Функция %s успешно завершилась", reader_file_transactions_xlxs.__name__)
        return transactions
    except Exception as ex:
        logger.error("Произошла ошибка %s", ex)
        return []
