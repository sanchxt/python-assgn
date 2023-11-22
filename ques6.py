def smallest_largest(inp_list):
    if not inp_list:
        print("The list is empty.")
        return

    smallest = float('inf')
    largest = float('-inf')

    for number in inp_list:
        smallest = min(smallest, number)
        largest = max(largest, number)

    print(f"Smallest Number: {smallest}")
    print(f"Largest Number: {largest}")


num_list = [12, 2, 7, 13, 16, 9]
smallest_largest(num_list)
