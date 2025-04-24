from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_method: str) -> Any:
    """Функция возвращает строку с замаскированным номером.
    Для карт и счетов используется разные типы маскировки"""
    if payment_method.startswith("Счет"):
        return (
                payment_method[:payment_method.find(" ")]
                + " "
                + get_mask_account(payment_method[payment_method.find(" "):])
        )
    else:
        return payment_method[:-16] + " " + get_mask_card_number(payment_method[-16:])


def gate_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")."""
    return ".".join(date[:10].split("-")[::-1])
