# Проект "Виджет"
## Описание:
Это виджет, который показывает несколько последних успешных банковских операций клиента.
## Установка:
* Клонируйте репозиторий:
  ```
  https://github.com/MrchknRV/Python_Homework.git
  ```
* Установите `poetry`
  ```
  pip install poetry
  ```
  Если `poetry` установлен, установите зависимости:
  ```
  # для первичной установки
  poetry install
  # для обновления
  poetry update
  ```
  Для просмотра установленных зависимостей используйте `poetry show --tree`
### Как работать
В данный момент готовы функции:
* `get_mask_card_number`, которая
принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате XXXX XX** **** XXXX, 
где X — это цифра номера. То есть видны первые 6 цифр и последние 4 цифры, остальные символы отображаются звездочками, номер разбит по блокам по 4 цифры, разделенным пробелами. Пример работы функции:
  ```
  7000792289606361     # входной аргумент
  7000 79** **** 6361  # выход функции
  ```
* `get_mask_account`, которая принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера. То есть видны только последние 4 цифры номера, а перед ними — две звездочки. Пример работы функции:
  ```
  73654108430135874305  # входной аргумент
  **4305  # выход функции
  ```
* В модуле `widget`, готова функция `mask_account_card`, которая которая умеет обрабатывать информацию как о картах, так и о счетах.
  Для карт и счетов используют разные типы маскировок описанные ранее.
  Так же в этом же модуле реализована функция `get_date`
* В модуле `processing`, готова функция `filter_by_state`, которая принимает список словарей и опционально значение для ключа `state` (по умолчанию 'EXECUTED').
  Функция возвращает новый список словарей, содержащий только те словари, у которых ключ `state` соответствует указанному значению.
  Так же в этом же модуле реализована функция `sort_by_date`, которая принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание). Возвращает новый список, отсортированный по дате (`date`).
