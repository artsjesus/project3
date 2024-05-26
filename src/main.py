from utils import load_operation, number_card
import re


def main():
    operations = load_operation()
    for operation in operations:
        operation_date = operation["date"].strftime("%d.%m.%Y")
        operations_name_to = re.sub("[^a-zA-ZА-Яа-я\s]", "", operation["to"])
        operations_number_to = re.sub("[\D]", "", operation["to"])
        operations_output_to = number_card(operations_name_to, operations_number_to)
        if "from" in operation:
            operations_name_card = re.sub("[^a-zA-ZА-Яа-я\s]", "", operation["from"])
            operations_number_card = re.sub("[\D]", "", operation["from"])
            card_output = number_card(operations_name_card, operations_number_card)
            print(f"{operation_date}, {operation["description"]}\n"
                  f"{operations_name_card}{card_output}->{operations_name_to}{operations_output_to}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{operation_date}, {operation["description"]}\n"
                  f"{operations_name_to}{operations_output_to}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")


if __name__ == '__main__':
    main()
