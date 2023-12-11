from src.open_file import open_file
from src.hide_the_account_or_card import hide_the_account_or_card
from src.converts_date import converts_date


def show_result():
    for i in open_file():
        print(converts_date(i["date"]), i["description"])
        if i['description'] == 'Открытие вклада':
            print(hide_the_account_or_card(i["to"]))
        else:
            print(f'{hide_the_account_or_card(i["from"])} -> {hide_the_account_or_card(i["to"])}')
        print(i["operationAmount"]["amount"], i["operationAmount"]["currency"]["name"])
        print(' ')


show_result()
