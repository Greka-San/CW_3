import json


def open_file():
    with open('operations.json', encoding='UTF-8') as file:
        list_of_operations = json.load(file)
        successful_operations = []
        for operation in list_of_operations:
            if 'state' in operation:
                if operation['state'] == 'EXECUTED':
                    successful_operations.append(operation)
        recent_transactions = sorted(successful_operations, key=lambda operations: operations["date"])
        last_transactions = recent_transactions[-5:len(recent_transactions)]
        return last_transactions
