# Suppose we are comparing implementations of insertion sort and merge sort on the same machine. 
# For inputs of size n, 
# insertion sort runs in 8n^2 steps, 
# while merge sort runs in 64nlog(n) steps. 
# For which values of n does insertion sort beat merge sort?

# find n that 8n^2 < 64nlog(n)
# n < 8log(n)
# n/8 < log(n)
# 2^n < n^8

n = 2
while True:
    if pow(2, n) > pow(n, 8):
        print("if n >=", n)
        print("merge sort win")
        break;
    else:
        n += 1
