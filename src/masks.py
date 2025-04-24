LEN_CARD_NUMBER: int = 16
LEN_MAX_ACCOUNT_NUMBER: int = 34


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    if LEN_CARD_NUMBER == len(card_number) and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return "Вы ввели некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if 0 < len(account_number) <= 34:
        return f"**{account_number[-4:]}"
    return "Вы ввели некорректный номер счета"
