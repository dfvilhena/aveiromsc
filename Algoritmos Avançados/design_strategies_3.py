import matplotlib.pyplot as plt
import random
import statistics as st

##### The Guessing Game

TEST_TOTAL = 100000
LOWER_BOUND = 1
UPPER_BOUND = 100

# Guessing between a and b
def guessing(a, b, k=0):
    k += 1
    guess = random.randint(a, b)
    if guess > choice:
        return guessing(a, guess, k)
    if guess < choice:
        return guessing(guess, b, k)
    return k

test_results = []

for i in range(0, TEST_TOTAL):
    choice = random.randint(LOWER_BOUND, UPPER_BOUND)
    k = guessing(LOWER_BOUND, UPPER_BOUND)
    test_results.append(k)


print("Minimum number of attempts: %d" % min(test_results))
print("Maximum number of attempts: %d" % max(test_results))
print("Average number of attempts: %d" % (sum(test_results)/len(test_results)))
print("Median number of attempts: %d" % st.median(test_results))


plt.hist(test_results, bins=30)
plt.show()

#####
