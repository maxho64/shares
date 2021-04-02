from Position import Position
from SberXLSPArser import SberXLSParser


class TradesParser(SberXLSParser):

    def __init__(self, file_path):
        super().__init__(file_path)

    def parse(self):
        df = self._get_data()

        for index, row in df.iterrows():
            position = Position(row)
            self.parsed_data.append(position)

    def get_data(self):
        return self.parsed_data
