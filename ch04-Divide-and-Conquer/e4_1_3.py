# Implement both the brute-force and recursive algorithms 
# for the maximum-subarray problem on your own computer. 
# What problem size n0 gives the crossover point 
# at which the recursive algorithm beats the brute-force algorithm? 
# Then, change the base case of the recursive algorithm 
# to use the brute-force algorithm whenever the problem size is less than n0
# Does that change the crossover point?
import random
import time
from e4_1_2 import bruteFindMaxSeq

def findMaxCrossSub(A, low, mid, high):
    max_left_sum = -float("inf")
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > max_left_sum:
            max_left_sum = sum
            max_left = i
    max_right_sum = -float("inf")
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += A[j]
        if sum > max_right_sum:
            max_right_sum = sum
            min_right = j
    return(max_left, min_right, max_left_sum + max_right_sum)

def findMaxSub(A, low, high):
    if low == high:
        # print("base case:", A[low:high+1])
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = findMaxSub(A, low, mid)
        (right_low, right_high, right_sum) = findMaxSub(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = findMaxCrossSub(A, low, mid, high)

        # print(low, mid, high)
        # print(A[low: high + 1])
        # print(" left:", left_low, "to", left_high, ":", left_sum)
        # print("right:", right_low, "to", right_high, ":", right_sum)
        # print("cross:", cross_low, "to", cross_high, ":", cross_sum)
        
        if left_sum >= right_sum and left_sum >= cross_sum:
            # print(":", left_sum)
            return (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            # print(":", right_sum)
            return (right_low, right_high, right_sum)
        else:
            # print(":", cross_sum)
            return (cross_low, cross_high, cross_sum)

if __name__ == "__main__":
    for n in range(2, 101):
        random.seed(10)
        A = random.sample(range(-20, 21), n)
        # print(A)
        t1 = time.time()
        recur = (recur_low, recur_high, recur_sum) = findMaxSub(A, 0, n - 1)
        t2 = time.time()
        brute = (brute_low, brute_high, brute_sum) = bruteFindMaxSeq(A)
        t3 = time.time()
        if recur_sum == brute_sum: 
            print(n, ": OK")
        else: 
            print(n, ": WRONG")
            print(A)
            print("recur:", recur)
            print("brute:", brute)
            break
        print("recur:", t2 - t1)
        print("brute:", t3 - t2)
        if t2 - t1 < t3 - t2:
            print("=====> ans:", n)
            print(A)
            print(recur)
            break
        print("=" * 30)


    # A = [8, -4, 3, -4, 4, 5, 1]
    # (left, right, sum) = findMaxSub(A, 0, 6)
    # print(" left:", left)
    # print("right:", right)
    # print("  sum:", sum)

        

