import logging

from config import PATH

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(PATH / "logs" / "masks.log", "w", encoding="UTF-8")
file_formatter = logging.Formatter(
    "[%(asctime)s.%(msecs)03d] [%(levelname)-7s] - %(name)r - (%(filename)s).%(funcName)s:%(lineno)-3d - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

LEN_CARD_NUMBER: int = 16
LEN_MAX_ACCOUNT_NUMBER: int = 35


def get_mask_card_number(card_number: str) -> str:
    logger.warning("Функция %s запущена с данными: %s", get_mask_card_number.__name__, card_number)
    """Функция принимает на вход номер карты и возвращает ее маску."""
    try:
        logger.debug("Проверка условия")
        if LEN_CARD_NUMBER == len(card_number) and card_number.isdigit():
            logger.info("Функция %s успешно завершила работу", get_mask_card_number.__name__)
            return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    except Exception as ex:
        logger.error("Функция %s завершила работу с ошибкой: %s", get_mask_card_number.__name__, ex)
    else:
        logger.warning("Некорректные данные на входе в функцию %s", get_mask_card_number.__name__)
        return "Вы ввели некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    logger.warning("Функция %s запущена с данными: %s", get_mask_account.__name__, account_number)
    """Функция принимает на вход номер счета и возвращает его маску."""
    try:
        logger.debug("Проверка условия")
        if 0 < len(account_number) < LEN_MAX_ACCOUNT_NUMBER:
            logger.info("Функция %s успешно завершила работу", get_mask_account.__name__)
            return f"**{account_number[-4:]}"
    except Exception as ex:
        logger.error("Функция %s завершила работу с ошибкой: %s", get_mask_card_number.__name__, ex)
    else:
        logger.warning("Некорректные данные на входе в функцию %s", get_mask_account.__name__)
        return "Вы ввели некорректный номер счета"
