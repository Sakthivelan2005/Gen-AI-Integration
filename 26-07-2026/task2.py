#Fibonacci series
def fibonacci(n):
    if(n==0):
        return 0
    elif n == 1:
        return 1
        # Recursive case: sum of the two previous terms
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(18))