from config import PATH
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.utils import get_financial_transaction_data
from src.csv_xlsx_reader import reader_file_transactions_csv, reader_file_transactions_xlxs

BASIC_JSON_FILE_DIR = PATH / "data" / "operations.json"
BASIC_DATA_FILE_CSV = PATH / "data" / "transactions.csv"
BASIC_DATA_FILE_XLSX = PATH / "data" / "transactions_excel.xlsx"

transaction_file = {
    "1": BASIC_JSON_FILE_DIR,
    "2": BASIC_DATA_FILE_CSV,
    "3": BASIC_DATA_FILE_XLSX
}

transaction_mode = {
    "1": get_financial_transaction_data,
    "2": reader_file_transactions_csv,
    "3": reader_file_transactions_xlxs
}


def main():
    file_data = ''
    result_data = []
    print("""Программа: Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")
    while True:
        user_choice = input("> ").strip()
        if user_choice not in transaction_file:
            print("Вы выбрали не верный формат. Попробуйте ещё раз")
            continue
        else:
            file_data = transaction_mode.get(user_choice)(transaction_file.get(user_choice))
            break
    print("Введите статус, по которому необходимо выполнить фильтрацию."
          " Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    user_status = input("> ").upper().strip()
    while user_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {user_status} не доступен.\nПопробуйте ещё раз")
        user_status = input("> ").upper().strip()
    else:
        result_data = filter_by_state(file_data, user_status)
    user_choice_sort = input("Отсортировать операции по дате? Да/Нет\n> ").lower().strip()
    while user_choice_sort not in ['да', 'нет']:
        user_choice_sort = input("Выберите ДА/НЕТ\n> ").lower().strip()
    else:
        if user_choice_sort == 'да':
            user_choice_sort_reverse = input(
                "Отсортировать по возрастанию или по убыванию?По возрастанию/По убыванию\n> ").lower()
            if user_choice_sort_reverse == 'по возрастанию':
                result_data = sort_by_date(result_data, False)
            else:
                result_data = sort_by_date(result_data)
    user_filter_valute = input("Выводить только рублевые транзакции? Да/Нет\n> ")
    while user_filter_valute not in ['да', 'нет']:
        user_filter_valute = input("Выберите ДА/НЕТ\n> ").lower().strip()
    else:
        if user_filter_valute == 'да':
            result_data = [item for item in filter_by_currency(result_data, "RUB")]

    print("Распечатываю итоговый список транзакций...")
    if len(result_data) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    print(f"Всего банковских операций в выборке: {len(result_data)}")


if __name__ == "__main__":
    main()
