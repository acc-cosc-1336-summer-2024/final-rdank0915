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