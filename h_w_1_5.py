# Write a Python program to get the Fibonacci series between 0 to 50.
def fibonacci(n):
    x = 0
    y = 1
    if n == 1:
        print(x)
    else:
        print(x)
        print(y)
        for i in range(2,n):
            z = x + y
            x =y
            y = z
            print(z)

fibonacci(10)