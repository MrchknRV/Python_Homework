from unittest.mock import Mock, patch

import pytest

from src.external_api import transaction_amount

USD_TRANSACTION = {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}
INVALID_TRANSACTION = {"wrong_key": {"amount": 100}}
SUCCESS_CONVERSION = {"success": True, "result": "7999.54"}
FAILED_CONVERSION = {"error": {"code": "invalid_api_key", "message": "Invalid API key"}}


@pytest.fixture
def get_mock_requests():
    with patch("requests.get") as mock_get:
        yield mock_get


def test_transactions_rub():
    result = transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
    assert result == "31957.58"


def test_invalid_transaction(capsys):
    result = transaction_amount(INVALID_TRANSACTION)
    captured = capsys.readouterr()
    assert "Key not found" in captured.out
    assert result is None


def test_usd_transaction_success(get_mock_requests):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = SUCCESS_CONVERSION
    get_mock_requests.return_value = mock_response

    result = transaction_amount(USD_TRANSACTION)
    assert result == "7999.54"
    get_mock_requests.assert_called_once()


def test_api_request_failure(get_mock_requests):
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.json.return_value = FAILED_CONVERSION
    get_mock_requests.return_value = mock_response

    result = transaction_amount(USD_TRANSACTION).split("\n")
    assert "Не успешный запрос." == result[0]
    assert "Код ошибки: 401 - invalid_api_key." == result[1]


def test_api_url_correctness(get_mock_requests):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = SUCCESS_CONVERSION
    get_mock_requests.return_value = mock_response

    transaction_amount(USD_TRANSACTION)

    args, kwargs = get_mock_requests.call_args
    assert "https://api.apilayer.com/exchangerates_data/convert" in args[0]
    assert "to=RUB" in args[0]
    assert "from=USD" in args[0]
    assert "amount=100" in args[0]
