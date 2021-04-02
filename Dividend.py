class Dividend(object):

    def __init__(self, row):
        self.total = row['Сумма']
        self.init_date = row['Дата подачи поручения']
        self.result_date = row['Дата исполнения поручения']
        self.operation = row['Содержание операции']

    def get_total(self):
        return self.total

    def get_init_date(self):
        return self.init_date

    def get_operation(self):
        return self.operation

    def get_result_date(self):
        return self.result_date

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return (f"Dividend:"
                f" Сумма: {self.total},"
                f" Дата подачи поручения: {self.init_date},"
                f" Дата исполнения поручения: {self.result_date},"
                f" Содержание операции: {self.operation}")
