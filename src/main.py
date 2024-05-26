from utils import load_operation, number_output, transaction, transaction_from


def main():
    operations = load_operation()
    for operation in operations:
        transfer = transaction(operation)
        if "from" in operation:
            transfer_from = transaction_from(operation["from"])

            if "Счет " == transfer_from.card_name():
                print(f"{transfer.date}, {operation["description"]}\n"
                      f"{transfer_from.card_name()}{transfer_from.account_number()}->{transfer.name_to()}{transfer.account_number()}\n"
                      f"{transfer.amount} {transfer.name}\n")
            else:
                card_output = number_output(transfer_from.card_number())
                print(f"{transfer.date}, {operation["description"]}\n"
                      f"{transfer_from.card_name()}{card_output}->{transfer.name_to()}{transfer.account_number()}\n"
                      f"{transfer.amount} {transfer.name}\n")

        else:
            print(f"{transfer.date}, {operation["description"]}\n"
                  f"{transfer.name_to()}{transfer.account_number()}\n"
                  f"{transfer.amount} {transfer.name}\n")


if __name__ == '__main__':
    main()
