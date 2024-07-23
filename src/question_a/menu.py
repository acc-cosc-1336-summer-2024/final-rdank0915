import question_a

def display_menu():
    print("Final Menu")
    print("1-Stock Purchase History")
    print("2-Exit")

def run_menu():
    option = "1"
    while(option != "2"):
        display_menu()
        option = input("Enter your menu option: ")
        if option == '2':
            print("Exiting the program...")
            break
        handle_menu_option(option)

def handle_menu_option(option):
    if(option == '1'):
        option_1()
    else:
        print("Invalid Option")

def option_1():
    
    stock_list = question_a.Stock()

    stock_list.stock_purchase_history()
    list = (stock_list)
    print(list)

    choice = "Y"
    while(choice == "Y" or choice == "N"):
        choice = input("Would you like to exit Y or N: ")
        if choice == "Y":
            print(option_1())
        elif choice == "N":
            print(run_menu())