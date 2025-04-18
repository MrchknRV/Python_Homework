LEN_CARD_NUMBER: int = 16


def get_mask_card_number(card_number: str) -> str:
    """Функция ринимает на вход номер карты и возвращает ее маску."""

    if LEN_CARD_NUMBER == len(card_number):
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    else:
        return "Вы ввели некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    return f"**{account_number[-4:]}"


# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("7000792289606361"))
