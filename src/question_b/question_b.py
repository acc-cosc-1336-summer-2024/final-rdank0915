#write functions here, don't add input('') statements here!

#Create a create_multiplication_table function that returns a list
def create_multiplication_table(rows, cols):

    list = []

    for i in range(0, rows):
        row_list = []
        for j in range(0, cols):
            row_list.append((i+1) * (j+1))
        list.append(row_list)

    return(list)

#Create a display_multiplication_table that displays a table and accepts a list parameter
def display_multiplication_table(list):
    for row in list:
        print(row)

def display_menu():
    print("Question B Menu")
    print("1-Create a multiplication matrix")
    print("2-Exit")

def run_menu():
    option = "1"
    while(option != "2"):
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

    rows = int(input("How many rows in your matrix?: "))
    cols = int(input("How many columns in your matrix?: "))
    list = create_multiplication_table(rows, cols)
    table = display_multiplication_table(list)
    print(table)
    

    choice = "Y"
    while(choice == "Y" or choice == "N"):
        choice = input("Would you like to exit Y or N: ")
        if choice == "Y":
            print(run_menu())
        elif choice == "N":
            print(option_1())

def option_2():
    print("Exiting the program...")