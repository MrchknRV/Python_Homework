import json
import logging
import os

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/utils.log', "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

BASIC_JSON_FILE_DIR = os.path.abspath(r"..\data\operations.json")
logger.info("Получаем путь до файла записи транзакций: %s", BASIC_JSON_FILE_DIR)


def get_financial_transaction_data(file_dir: str) -> list:
    logger.warning("Функция %s запущена", get_financial_transaction_data.__name__)
    """Функция, которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях.
     Если файл пустой, содержит не список или не найден, функция возвращает пустой список"""
    try:
        logger.info("Записываем данные в файл %s", file_dir)
        with open(file_dir, "r", encoding="UTF-8") as json_file:
            json_data = json.load(json_file)
            logger.debug("Проверка условия")
            if not isinstance(json_data, list):
                logger.warning("Проверка не прошла")
                logger.info("Функция %s завершает работу со значением: []", get_financial_transaction_data.__name__)
                return []
            logger.info("Функция %s успешно завершилась", get_financial_transaction_data.__name__)
            return json_data
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.error("Произошла ошибка %s", ex)
        logger.warning("Функция %s завершилась аварийно", get_financial_transaction_data.__name__)
        return []
