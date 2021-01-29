fib_dict = {0: 0,
    1: 1}

array_size = 20
fib_array = [-1] * array_size
fib_array[0] = 0
fib_array[1] = 1

def fibonacci_number_rec(n):
    if n <= 1:
        return n
    fibonacci_number_rec.counter += 1
    return fibonacci_number_rec(n-1)+fibonacci_number_rec(n-2)

def fibonacci_number_dict(n):
    if n in fib_dict:
        return fib_dict[n]
    fibonacci_number_dict.counter += 1
    fib_dict[n] = fibonacci_number_dict(n-1)+fibonacci_number_dict(n-2)
    return fib_dict[n]

def fibonacci_number_array(n):
    if fib_array[n] != -1:
        return fib_array[n]
    fibonacci_number_array.counter += 1
    fib_array[n] = fibonacci_number_array(n-1)+fibonacci_number_array(n-2)
    return fib_array[n]

fibonacci_number_rec.counter = 0
fibonacci_number_dict.counter = 0
fibonacci_number_array.counter = 0
n = 10
print("The %d-th Fibonacci number is %d and took %d fuction calls using pure recursion" % (n,fibonacci_number_rec(n), fibonacci_number_rec.counter))
print("The %d-th Fibonacci number is %d and took %d fuction calls using a dictionary" % (n,fibonacci_number_dict(n), fibonacci_number_dict.counter))
print("The %d-th Fibonacci number is %d and took %d fuction calls using an array" % (n,fibonacci_number_array(n), fibonacci_number_array.counter))