import pytest
@pytest.fixture
def operations_json():
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "26.08.2018",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]