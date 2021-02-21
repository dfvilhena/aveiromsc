##### Brute Force

def iter_power(a, b):
    r = 1
    #if b==0: return 1
    for i in range(0, b):
        r *= a
    return r

def rec_power(a, b):
    if b==0: return 1
    return a*rec_power(a, b-1)

##### Divide and Conquer

def div_conq_power(a, b):
    if b==0: return 1
    if b==1: return a
    return div_conq_power(a, b//2)*div_conq_power(a, (b+1)//2)

##### Decrease and Conquer

def dec_conq_power(a, b):
    if b==0: return 1
    if b==1: return a
    p = dec_conq_power(a, b//2)
    if b%2==0: return p*p
    return a*p*p

def iter_dec_conq_power(a, b):
    r = 1
    for i in range(0, b//2):
        r *= a
    if b%2==0: return r*r
    return a*r*r

##### Counting even values in array

def count_bf(int_list):
    k = 0
    for number in int_list:
        if number%2==0: k += 1
    return k

def count_div(int_list):
    if len(int_list) == 0: return 0
    if len(int_list) == 1: return 1-int_list[0]%2
    return count_div(int_list[:len(int_list)//2])+count_div(int_list[len(int_list)//2:]) 

def count_dec(int_list):
    if len(int_list) == 0: return 0
    if len(int_list) == 1: return 1-int_list[0]%2
    k1 = count_div(int_list[:len(int_list)//2])
    k2 = count_div(int_list[len(int_list)//2:2*(len(int_list)//2)])
    if len(int_list) > 1 and len(int_list)%2 == 0:
        return k1+k2
    return k1+k2+1-int_list[-1]%2



int_list = range(1, 7975766)
print(count_bf(int_list))
print(count_div(int_list))
print(count_dec(int_list))
