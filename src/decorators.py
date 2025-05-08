from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., str]], Callable[..., str]]:
    """Декоратор для логирования вызовов функций."""

    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> str:
            start_loging = f"Функция {func.__name__} была вызвана с аргументами {args}, {kwargs}\n"

            if filename:
                with open("filename.txt", "a", encoding="utf-8") as f:
                    f.write(start_loging)
            else:
                print(start_loging.strip())
            try:
                res = func(*args, **kwargs)
                successful_loging = f"Результат функции '{func.__name__}': {res}\n"
                if filename:
                    with open("filename.txt", "a", encoding="utf-8") as f:
                        f.write(successful_loging)
                else:
                    print(successful_loging.strip())
                return res
            except Exception as exc:
                error_loging = (
                    f"Функция {func.__name__} завершила работу с ошибкой\n"
                    f"Ошибка выполнения: {type(exc).__name__}: {exc}. Аргументы: {args}, {kwargs}\n"
                )
                if filename:
                    with open("filename.txt", "a", encoding="utf-8") as f:
                        f.write(error_loging.strip())
                else:
                    print(error_loging)
                raise

        return inner

    return decorator
