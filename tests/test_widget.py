import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет BY20 OLMP 3135 0000 0010 0000 0933", "Счет **0933"),
    ],
)
def test_mask_account_card(test_input: str, expected: str) -> None:
    assert mask_account_card(test_input) == expected


def test_mask_account_card_invalid() -> None:
    assert mask_account_card("") == "Вы ввели некорректный номер карты"
    assert mask_account_card("Счет") == "Вы ввели некорректный номер счета"
    assert mask_account_card("Visa Platinum 7000792asfasf06361") == "Вы ввели некорректный номер карты"
    assert (
        mask_account_card("Счет BY20 OLMP 3135 0000 0010 0000 0933BY20 OLMP 3135 0000 0010 0000 0933")
        == "Вы ввели некорректный номер счета"
    )
