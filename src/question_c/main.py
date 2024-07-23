#add import

import question_c

class Portfolio:

    def __init__(self, name):
        self.__name = name
        self.__stocks = []
    
    def add_stock(self, stock):
        self.__stocks.append(stock)
    
    def display_portfolio(self):
        print(f"Stock Portfolio: {self.__name}")
        for stock in self.__stocks:
            print(f"{stock.get_symbol()} - {stock.get_company_name()}")