from currency.repositories import GetterExchangeRate

class ExchangeRateController:
    def __init__(self):
        self.base = GetterExchangeRate.get()

    def get(self):
        enum = enumerate(self.base, 1)
        return enum

