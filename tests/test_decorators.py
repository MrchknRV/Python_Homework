import pytest

from src.decorators import log


def test_console_logging_success(capsys) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    res = add(2, 3)
    captured = capsys.readouterr()
    raws = captured.out.split("\n")

    assert "Функция add была вызвана с аргументами (2, 3), {}" == raws[0]
    assert "Результат функции 'add': 5" == raws[1]
    assert res == 5


def test_console_logging_error(capsys) -> None:
    @log()
    def error_func() -> None:
        raise TypeError("Какая-то ошибка")

    with pytest.raises(TypeError):
        error_func()

    captured = capsys.readouterr()
    raws = captured.out.split("\n")

    assert "Функция error_func была вызвана с аргументами (), {}" == raws[0]
    assert "Функция error_func завершила работу с ошибкой" == raws[1]
    assert "Ошибка выполнения: TypeError: Какая-то ошибка. Аргументы: (), {}" == raws[2]


def test_console_empty_logging(capsys) -> None:
    @log()
    def empty_func() -> None:
        return None

    res = empty_func()
    captured = capsys.readouterr()
    raws = captured.out.split("\n")

    assert "Функция empty_func была вызвана с аргументами (), {}" == raws[0]
    assert "Результат функции 'empty_func': None" == raws[1]
    assert res is None


def test_file_logging_success() -> None:
    @log(filename="test_logging")
    def multiply(a: int, b: int) -> int:
        return a * b

    result = multiply(4, 5)

    with open("test_logging", "r", encoding="utf-8") as f:
        content = f.read().split("\n")
        assert "Функция multiply была вызвана с аргументами (4, 5), {}" == content[0]
        assert "Результат функции 'multiply': 20" == content[1]

    assert result == 20


def test_file_logging_error() -> None:
    @log(filename="error_logging")
    def error_func(x: int) -> None:
        raise ValueError(f"Неверное значение: {x}")

    with pytest.raises(ValueError):
        error_func(32)

    with open("error_logging", "r", encoding="utf-8") as f:
        content = f.read().split("\n")
        assert "Функция error_func была вызвана с аргументами (32,), {}" == content[0]
        assert "Функция error_func завершила работу с ошибкой" == content[1]
        assert "Ошибка выполнения: ValueError: Неверное значение: 32. Аргументы: (32,), {}" == content[2]


def test_keyword_arguments_logging(capsys) -> None:
    @log()
    def kwargs_element_func(name: str, job) -> str:
        return f"{name.title()} is {job.title()}"

    res = kwargs_element_func("Rodion", job="developer")

    captured = capsys.readouterr()
    raws = captured.out.split("\n")

    assert "Функция kwargs_element_func была вызвана с аргументами ('Rodion',), {'job': 'developer'}" == raws[0]
    assert "Результат функции 'kwargs_element_func': Rodion is Developer" == raws[1]
    assert res == "Rodion is Developer"


def test_function_metadata() -> None:
    @log()
    def sample_func(a: int) -> str:
        """Sample function docstring"""
        return str(a)

    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "Sample function docstring"
