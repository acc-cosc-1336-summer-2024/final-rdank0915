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
        
#Create a function stock_list with 5 variables/instances of Stock
#with the values from the Stock List
def stock_list():

    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

   