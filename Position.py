class Position(object):

    def __init__(self, sec_id, price, amount, purchase_date, transaction_fee=0.0, moex_fee=0.0):
        self.sec_id = sec_id
        self.transaction_fee = transaction_fee
        self.moex_fee = moex_fee
        self.price = price
        self.amount = amount
        self.purchase_date = purchase_date

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

    def set_amount(self, amount):
        self.amount = amount

    def get_purchase_date(self):
        return self.purchase_date

    def __str__(self):
        return (f"Position :"
                f" Код: {self.sec_id},"
                f" Цена: {self.price},"
                f" Количество: {self.amount},"
                f" Дата расчётов: {self.purchase_date},"
                f" Комиссия торговой системы: {self.moex_fee},"
                f" Комиссия банка: {self.transaction_fee}")