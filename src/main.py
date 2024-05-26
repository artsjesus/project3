from utils import load_operation
import re


def main():
    operations = load_operation()
    for operation in operations:
        operation_date = operation["date"].strftime("%d.%m.%Y")
        operations_name_to = re.sub("[^a-zA-ZА-Яа-я\s]", "", operation["to"])
        operations_number_to = re.sub("[\D]", "", operation["to"])
        if "from" in operation:
            operations_name_card = re.sub("[^a-zA-ZА-Яа-я\s]", "", operation["from"])
            operations_number_card = re.sub("[\D]", "", operation["from"])
            operations_number_card = list(operations_number_card)
            print(operations_name_card)
            if operations_name_card != "Счет ":
                for index, item in enumerate(operations_number_card):
                    if 5 < index < 12:
                        operations_number_card[index] = "*"
                operations_number_card.insert(4, " ")
                operations_number_card.insert(9, " ")
                operations_number_card.insert(14, " ")
                operations_number_card.insert(19, " ")
                operations_number_card = "".join(operations_number_card)
            else:
                "".join(operations_number_card)
                operations_number_card = "**" + operations_number_to[-4:]
            print(f"{operation_date}, {operation["description"]}\n"
                  f"{operations_name_card}{operations_number_card}->{operations_name_to}**{operations_number_to[-4:]}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{operation_date}, {operation["description"]}\n"
                  f"->{operations_name_to} **{operations_number_to[-4:]}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")


if __name__ == '__main__':
    main()
