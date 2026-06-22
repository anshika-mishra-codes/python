marks = input("Enter marks: ")
marks = int(marks)

if marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
elif marks >= 60:
    print("C grade")
elif marks >= 40:
    print("D grade")
else:
    print("Please Try Harder")