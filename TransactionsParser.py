from Dividend import Dividend
from SberXLSPArser import SberXLSParser


class TransactionsParser(SberXLSParser):

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self):
        df = self._get_data()

        for index, row in df.iterrows():
            if row['Операция'] == 'Зачисление дивидендов':
                dividend = Dividend(row)
                self.parsed_data.append(dividend)

    def get_data(self):
        return self.parsed_data
