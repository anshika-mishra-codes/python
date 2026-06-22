numbers = (1, 2, 2, 3, 4, 2, 5)

num = int(input("Enter number to find: "))

count = 0

for i in numbers:
    if i == num:
        count = count + 1

print("Occurrences:", count)