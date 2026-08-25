def Triangle(num):
    rows = num
    for i in range(rows, 0, -1):
        print("* " * i)
    return 0

num = int(input("Enter an integer number: "))
Triangle(num)

