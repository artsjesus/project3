import json
from dateutil import parser


def load_operation():
    operations = []
    with open("operations.json", "r", encoding="UTF-8") as file:
        operation_list = [operation for operation in json.load(file) if operation and operation["state"] == "EXECUTED"]
    operation_list.sort(key=lambda x: str(x.get("date")), reverse=True)
    operation_list = operation_list[:5]

    for operation in operation_list:
        operation["date"] = parser.parse(operation["date"]).date()
        operations.append(operation)
    return operations
