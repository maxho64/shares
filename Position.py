class Position(object):

    def __init__(self, row):
        self.price = row['Цена']
        self.sec_id = row['Код финансового инструмента']
        self.purchase_date = row['Дата расчётов']
        self.amount = row['Количество']
        self.moex_fee = row['Комиссия торговой системы']
        self.transaction_fee = row['Комиссия банка']
        self.operation = row['Операция']

    def get_sec_id(self):
        return self.sec_id

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_transaction_fee(self):
        return self.transaction_fee

    def set_transaction_fee(self, transaction_fee):
        self.transaction_fee = transaction_fee

    def get_moex_fee(self):
        return self.moex_fee

    def set_moex_fee(self, moex_fee):
        self.moex_fee = moex_fee

    def get_amount(self):
        return self.amount

    def get_operation(self):
        return self.operation

    def set_amount(self, amount):
        self.amount = amount

    def get_purchase_date(self):
        return self.purchase_date

    def get_total(self):
        return round(self.price * self.amount, 2)

    def get_total_with_fee(self):
        return round(self.get_total() + self.transaction_fee + self.moex_fee, 2)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f"Position:"
                f" Код: {self.sec_id},"
                f" Цена: {self.price},"
                f" Количество: {self.amount},"
                f" Дата расчётов: {self.purchase_date},"
                f" Комиссия торговой системы: {self.moex_fee},"
                f" Операция: {self.operation},"
                f" Комиссия банка: {self.transaction_fee}")