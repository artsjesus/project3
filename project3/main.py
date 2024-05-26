from utils import load_operation

def main():
    operations = load_operation()
    for operation in operations:
        if "from" in operation:
            print(f"{operation["date"]}, {operation["description"]}\n"
                  f"{operation["from"]} -> **{operation["to"]}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{operation["date"]}, {operation["description"]}\n"
                  f"-> счёт {operation["to"]}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")


if __name__ == '__main__':
    main()