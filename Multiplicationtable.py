num = int(input("Enter a positive integer: "))
if num <= 0:
    print("Not a positive integer")
else:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
