#write functions here, don't add input('') statements here!

def num_list():

    nums = []

    print("You will be asked to enter 5 numbers...")
    
    for i in range(5):
        number = float(input(f"Enter number {i + 1}: "))
        nums.append(number)

    min_num = min(nums)
    max_num = max(nums)
    total = sum(nums)
    avg_num = total / len(nums)

    header_row = "{:<10}".format("Statistics")
    separator = "{:<10}".format(" ")

    print(separator)
    print(header_row)
    print(separator)

    print(f"Minimum: {min_num}")
    print(f"Maximum: {max_num}")
    print(f"Total: {total}")
    print(f"Average: {avg_num}")