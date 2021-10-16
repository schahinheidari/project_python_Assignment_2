n = int(input("please enter your number: : "))


sum = 0
x1, x2= 0, 1
if n <= 0:
    print("please enter a positive integer number...")
elif n == 1:
    print(1)
else:
    print("Fibonacci : ")
    while sum < n:
        print(x1)
        fib = x1 + x2
        x1 = x2
        x2= fib
        sum += 1
