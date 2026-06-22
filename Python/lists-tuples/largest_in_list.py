numbers = [10, 5, 8, 20, 3]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number is:", largest)