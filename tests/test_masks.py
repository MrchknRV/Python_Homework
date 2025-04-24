import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("7034790289216361", "7034 79** **** 6361"),
        ("700079228960636112", "Вы ввели некорректный номер карты"),
        ("", "Вы ввели некорректный номер карты"),
    ],
)
def test_masks(number: str, expected: str) -> None:
    assert get_mask_card_number(number) == expected


def test_masks_letters() -> None:
    assert get_mask_card_number("7000792sfa606361") == "Вы ввели некорректный номер карты"
    assert get_mask_card_number("70**792sa606361") == "Вы ввели некорректный номер карты"


@pytest.mark.parametrize(
    "number, expected",
    [
        ("7000792289606361", "**6361"),
        ("", "Вы ввели некорректный номер счета"),
        ("BY20 OLMP 3135 0000 0010 0000 0933", "**0933"),
        ("BY20 OLMP 3135 0000 0010 0000 0933BY20 OLMP 3135 0000 0010 0000 0933", "Вы ввели некорректный номер счета"),
    ],
)
def test_masks_accounts(number: str, expected: str) -> None:
    assert get_mask_account(number) == expected
