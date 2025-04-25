from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_method: str) -> Any:
    """Функция возвращает строку с замаскированным номером.
    Для карт и счетов используется разные типы маскировки"""
    if (
        payment_method.startswith("Счет")
        and payment_method.find(" ") == -1
        or get_mask_account(payment_method[payment_method.find(" ") + 1:]) == "Вы ввели некорректный номер счета"
    ):
        return "Вы ввели некорректный номер счета"
    elif payment_method.startswith("Счет"):
        return (
            payment_method[: payment_method.find(" ")]
            + " "
            + get_mask_account(payment_method[payment_method.find(" ") + 1:])
        )
    elif get_mask_card_number(payment_method[-16:]) == "Вы ввели некорректный номер карты":
        return "Вы ввели некорректный номер карты"
    return payment_method[:-16] + get_mask_card_number(payment_method[-16:])


def gate_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")."""
    if len(date) > 0 and "".join(date[:10].split("-")).isdigit():
        return ".".join(date[:10].split("-")[::-1])
    return "Вы ввели некорректную дату"
