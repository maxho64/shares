from Position import Position
from SberXLSPArser import SberXLSParser


class TransactionsParser(SberXLSParser):

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self):
        df = self.getData()

        for index, row in df.iterrows():

            price = row['Цена']
            sec_id = row['Код финансового инструмента']
            purchase_date = row['Дата расчётов']
            amount = row['Количество']
            moex_fee = row['Комиссия торговой системы']
            transaction_fee = row['Комиссия банка']
            operation = row['Операция']
            position = Position(sec_id, price, amount, operation, purchase_date, transaction_fee, moex_fee)
            print(row)
            return
