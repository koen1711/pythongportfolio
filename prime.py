import math

first = 1
last = 500

prime_numbers = []

if last == 1: 
    print("Not a prime number.")
else:
    for i in range(first, last):
        prime_flag = 0

        for x in range(2, int(math.sqrt(i)) + 1):
            if (i % x == 0):
                prime_flag = 1
                break

        if (prime_flag == 0) and (i != 1):
            prime_numbers.append(i)


print(set(prime_numbers))
