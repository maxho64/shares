from Position  import Position


class InvestmentPortfolio(object):

    def __init__(self):
        self.current_shares = list()

    def addShare(self, current_share: Position ):
        self.current_shares.append(current_share)
