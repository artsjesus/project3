import json
from dateutil import parser


def load_operation():
    """Создание списка операций"""
    operations = []
    with open("operations.json", "r", encoding="UTF-8") as file:
        operation_list = [operation for operation in json.load(file) if operation and operation["state"] == "EXECUTED"]
    operation_list.sort(key=lambda x: str(x.get("date")), reverse=True)
    operation_list = operation_list[:5]

    for operation in operation_list:
        operation["date"] = parser.parse(operation["date"]).date()
        operations.append(operation)
    return operations


def number_card(operations_name_card, operations_number_card):
    """Вывод номера карты или счета в нужном формате"""
    operations_number_card = list(operations_number_card)
    if operations_name_card != "Счет ":
        for index, item in enumerate(operations_number_card):
            if 5 < index < 12:
                operations_number_card[index] = "*"
        operations_number_card.insert(4, " ")
        operations_number_card.insert(9, " ")
        operations_number_card.insert(14, " ")
        operations_number_card.insert(19, " ")
        operations_number_card = "".join(operations_number_card)
        return operations_number_card
    else:
        operations_number_card = "".join(operations_number_card)
        operations_number_card = "**" + operations_number_card[-4:]
        return operations_number_card






