# What is the smallest value of n 
# such that an algorithm whose running time is 100n^2
# runs faster than an algorithm whose running time is 2^n 
# on the same machine?

# find n that 100n^2 < 2^n

n = 1
while True:
    if 100 * n * n < pow(2, n):
        print("if n >=", n)
        print("100n^2 < 2^n")
        break;
    else: 
        n += 1