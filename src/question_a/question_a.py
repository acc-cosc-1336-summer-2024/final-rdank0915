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
    stock_list = [
        Stock("AAPL", "Apple Inc."),
        Stock("CAT", "Caterpillar"),
        Stock("EK", "Eastman Kodak"),
        Stock("GOOG", "Google"),
        Stock("MSFT", "Microsoft")
        ]
    
    # Create a dictionary to hold the stocks
    stock_dict = {}
    
    #Add the 5 stock variables to a dictionary
    for stock in stock_list:
        stock_dict[Stock.get_symbol()] = Stock.get_company_name()

    print("Symbol:\n" + "\n".join(f"{symbol}" for symbol in stock_dict.keys()))
    print("\nCompany Name:\n" + "\n".join(f"{company_name}" for company_name in stock_dict.values()))
    