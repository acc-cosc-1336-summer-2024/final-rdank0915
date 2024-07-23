#write functions here, don't add input('') statements here!

class Stock:
    
    #Create a constructor that accepts symbol and company_name
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    #Create a stock class function/method that returns symbol
    def get_symbol(self):
        return self.__symbol
    
    #Create a stock class function/method that returns company_name
    def get_company_name(self):
        return self.__company_name
        

class StockList:

    def __init__(self):
        self.stocks = []
        self.add_stocks()
    
    def add_stocks(self):
        symbols = ["AAPL", "CAT", "EK", "GOOG", "MSFT"]
        company_names = ["Apple Inc", "Caterpillar", "Eastman Kodak", "Google", "Microsoft"]
        
        for i in range(len(symbols)):
            stock = Stock(symbols[i], company_names[i])
            self.stocks.append(stock)
    
    def display_stock_report(self):
        
        print("Company Stock Report")
        print()
        
        for stock in self.stocks:
            print(f"Company: {stock.get_company_name()}")
            print(f"Symbol: {stock.get_symbol()}")
            print()