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
        

class Portfolio:

    def __init__(self):
        self.stocks = []
        self.stock_list()
    
    def stock_list(self):
        symbol = ["AAPL", "CAT", "EK", "GOOG", "MSFT"]
        company_name = ["Apple Inc", "Caterpillar", "Eastman Kodak", "Google", "Microsoft"]
        
        for i in range(len(symbol)):
            stock = Stock(symbol[i], company_name[i])
            self.stocks.append(stock)
    
    def display_stock_report(self):
        
        print("Company Stock Report")
        print()
        
        for stock in self.stocks:
            print(f"Symbol: {stock.get_symbol()}")
            print(f"Company: {stock.get_company_name()}")
            print()