#write functions here, don't add input('') statements here!
def test_config():
    return True

#Create a class Stock with private variables symbol and company_name 
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
        
#Create a function stock_purchase_history with 5 variables/instances of Stock
#with the values from the Stock List
def stock_purchase_history():

    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")

    #Create a dictionary to hold the stocks and add the instances to it
    stock_dict = {
        "stock1": stock1,
        "stock2": stock2,
        "stock3": stock3,
        "stock4": stock4,
        "stock5": stock5
    }

    header_row = "{:<10} {:<20}".format("Symbol", "Company Name")

    print(header_row)

    #Add the 5 stock variables to a dictionary
    for key, stock in stock_dict.items():
        symbol = stock.get_symbol()
        company_name = stock.get_company_name()
        print("{:<10} {:<20}".format(symbol, company_name))
    
    