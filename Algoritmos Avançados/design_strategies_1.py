"""
TASK 1 - ITERATIONS
TASK 2 - RECURSION
"""


########################################### TASK 1 ################################################


# Return sum from 1 to n. Iterative, has n iterations
def f1(n):
    r = 0
    for i in range(1, n+1):
        r += i
    return r

# Return n^2  in an iterative fashion, with n^2 iterations
def f2(n):
    r = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            r += 1
    return r

# Return sum from 1 to n, with that same number of iterations
def f3(n):
    r = 0
    k = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            r += 1
            k += 1
    return r

# Return the sum of a sum (sum_m_from1ton{sum_p_from1tom}). number of iterations is n*(n+1)/2
def f4(n):
    r = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            r += j
    return r

########################################### TASK 2 ################################################

# Returns n with n recursive calls
def r1(n):
    if n==0: return 0
    return r1(n-1)+1

# Returns the sum of all even or odd numbers up to n, with n/2 recursive calls
def r2(n):
    if n==0: return 0
    if n==1: return 1
    return n+r2(n-2)

# Returns 2^n - 1, has n recursive calls
def r3(n):
    if n==0: return 0
    return 1+2*r3(n-1)

# Returns 2^n - 1, has 2(2^n -1) recursive calls
def r4(n):
    if n==0: return 0
    return 1+r4(n-1)+r4(n-1)
