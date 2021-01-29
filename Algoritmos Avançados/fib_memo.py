from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

n = 24
f = [-1]*(n+1)

def fibonacci_number(n):
    
    r = 0
    if f[n] != -1: return f[n]
    fibonacci_number.counter += 1
    if n == 1: r = 1
    elif n == 2: r = 1
    else:
        r = fibonacci_number(n-2)
        r = r+fibonacci_number(n-1)
    f[n] = r
    return r


fibonacci_number = memo(fibonacci_number)

fibonacci_number.counter = 0

print("The %d-th Fibonacci number is %d and took %d fuction calls using pure recursion" % (n,fibonacci_number(n), fibonacci_number.counter))
