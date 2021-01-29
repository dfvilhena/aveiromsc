def brute_force_pot(a,b):
    if b == 0:
        return 1
    brute_force_pot.counter += 1
    return a*brute_force_pot(a, b-1)

def div_conq_pot(a,b):
    if b == 0:
        return 1
    div_conq_pot.counter += 1
    if b == 1:
        return a
    return div_conq_pot(a, b//2)*div_conq_pot(a, (b+1)//2)

def dec_conq_pot(a,b):
    if b == 0:
        return 1
    dec_conq_pot.counter += 1
    p = dec_conq_pot(a, b//2)
    if b%2 == 0:
        return p*p
    return a*p*p

a = 2
b = 15

print("Calculating %d to the power of %d...\n" % (a, b))

print("Brute-Force")
brute_force_pot.counter = 0
print("Result: %d" % brute_force_pot(a,b))
print("There were %d function calls\n" % brute_force_pot.counter)

print("Divide-and-Conquer")
div_conq_pot.counter = 0
print("Result: %d" % div_conq_pot(a,b))
print("There were %d function calls\n" % div_conq_pot.counter)

print("Decrease-and-Conquer")
dec_conq_pot.counter = 0
print("Result: %d" % dec_conq_pot(a,b))
print("There were %d function calls\n" % dec_conq_pot.counter)