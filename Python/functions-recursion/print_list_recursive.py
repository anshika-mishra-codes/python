def print_list(lst, i=0):
    if i == len(lst):
        return

    print(lst[i])
    print_list(lst, i + 1)

numbers = [1, 2, 3, 4, 5]

print_list(numbers)