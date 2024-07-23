import question_a

def display_menu():
    print("Final Menu")
    print("1-Stock Purchase History")
    print("2-Exit")

def run_menu():
    option = "1"
    display_menu()
    option = input("Enter your menu option: ")
    handle_menu_option(option)

def handle_menu_option(option):
    if(option == '1'):
        option_1()
    elif(option == '2'):
        option_2()
    else:
        print("Invalid Option")

def option_1():
    
    list = question_a.stock_purchase_history()
    
    print(list)

    choice = "Y"
    while(choice == "Y"):
        choice = input("Enter Y to exit: ")
        if choice == "Y":
            print(run_menu())
            break
        else:
            print("Invalid Option")

def option_2():
    print("Exiting the program...")
    
