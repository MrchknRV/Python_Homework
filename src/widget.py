from typing import Any

from masks import get_mask_account, get_mask_card_number


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


# print(mask_account_card("Счет 73654108430135874305"))
# print(mask_account_card("Maestro 1596837868705199"))
# print(mask_account_card("Счет 64686473678894779589"))
# print(mask_account_card("MasterCard 7158300734726758"))
# print(mask_account_card("Visa Platinum 8990922113665229"))
# print(mask_account_card("Visa Gold 5999414228426353"))
# print(mask_account_card("Visa Classic 6831982476737658"))
# print(mask_account_card("Счет 73654108430135874305"))


def gate_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате
    "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате
    "ДД.ММ.ГГГГ"("11.03.2024")."""
    return ".".join(date[:10].split("-")[::-1])


# print(gate_date("2024-03-11T02:26:18.671407"))
# print(gate_date("2025-04-04T08:55:37.578201"))
