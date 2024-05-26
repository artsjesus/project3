import re


class Transaction():
    def __init__(self, date, description, to, amount, name):
        self.date = date
        self.description = description
        self.to = to
        self.amount = amount
        self.name = name

    def name_to(self):
        """На что переводим"""
        return re.sub("[^a-zA-ZА-Яа-я\s]", "", self.to)

    def number_to(self):
        """Номер счета на который переводим"""
        return re.sub("[\D]", "", self.to)

    def account_number(self):
        """Скрытие номера счета"""
        return "**" + self.number_to()[-4:]


class TransactionFrom(Transaction):
    def __init__(self, from_):
        self.from_ = from_

    def card_name(self):
        """Название карты"""
        return re.sub("[^a-zA-ZА-Яа-я\s]", "", self.from_)

    def card_number(self):
        """Номер карты счета с которого переводим"""
        return re.sub("[\D]", "", self.from_)

    def account_number(self):
        """Скрытие счета"""
        return "**" + self.card_number()[-4:]
