import pytest

from src.widget import gate_date, mask_account_card


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
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


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-10-26T14:06:85.312078", "26.10.2019"),
        ("2002-02-26T15:17:03.984523", "26.02.2002"),
        ("1945-05-09T09:23:55.162547", "09.05.1945"),
    ],
)
def test_gate_date(test_input: str, expected: str) -> None:
    assert gate_date(test_input) == expected


def test_gate_date_invalid() -> None:
    assert gate_date("") == "Вы ввели некорректную дату"
    assert gate_date("2014-**-AAT08:12:35:98745") == "Вы ввели некорректную дату"
    assert gate_date("test_text") == "Вы ввели некорректную дату"
