from unittest.mock import mock_open, patch

from src.csv_xlsx_reader import reader_file_transactions_csv

CSV_CONTENT = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту
"""
EXPECTED_RES = [
    {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    },
    {
        "id": "3598919",
        "state": "EXECUTED",
        "date": "2020-12-06T23:00:58Z",
        "amount": "29740",
        "currency_name": "Peso",
        "currency_code": "COP",
        "from": "Discover 3172601889670065",
        "to": "Discover 0720428384694643",
        "description": "Перевод с карты на карту",
    },
]


def test_success_reader_file_transactions_csv():
    with patch("builtins.open", mock_open(read_data=CSV_CONTENT)):
        result = reader_file_transactions_csv("test_path.csv")
        assert result == EXPECTED_RES


def test_reader_file_transactions_csv_empty_file():
    with patch("builtins.open", mock_open(read_data="")):
        result = reader_file_transactions_csv("empty_file.csv")
        assert result == []


def test_reader_file_transactions_csv_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError("File not found")):
        result = reader_file_transactions_csv("nonexistent_file.csv")
        assert result == []
