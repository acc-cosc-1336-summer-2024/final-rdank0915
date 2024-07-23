#add import

import question_b

rows = int(input("How many rows in your matrix?: "))
cols = int(input("How many columns in your matrix?: "))

list = question_b.create_multiplication_table(rows, cols)
table = question_b.display_multiplication_table(list)