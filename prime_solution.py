import math

a_number = 50

if a_number > 1:
    for i in range(2, int(math.sqrt(a_number))):
        if a_number % i == 0:
            print(a_number, "is divisible by", i)
            print(a_number, "is not a prime number")
            break
    else:
        print(a_number, "is a prime number")
else:
    print(a_number, "is not a prime number")
