import pandas as pd


class SberXLSParser(object):

    def __init__(self, file_path):
        self.file_path = file_path
        self.parsed_data = list()

    def _get_data(self):
        dfs = pd.read_excel(self.file_path, sheet_name=None)
        df = dfs[list(dfs.keys())[0]]
        return df
