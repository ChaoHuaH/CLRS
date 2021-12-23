# Use the following ideas to develop a nonrecursive, linear-time algorithm for the
# maximum-subarray problem. Start at the left end of the array, and progress toward
# the right, keeping track of the maximum subarray seen so far. Knowing a maximum
# subarray of A[1..j] , extend the answer to find a maximum subarray ending at index j + 1
# by using the following observation: a maximum subarray of A[1..j+1]
# is either a maximum subarray of A[1..j] or a subarray A[1..j+1], for some
# 1 <= i <= j + 1. Determine a maximum subarray of the form A[1..j+1] in
# constant time based on knowing a maximum subarray ending at index j.

"""
ITERATIVE-FIND-MAXIMUM-SUBARRAY(A)
n = A.length
max_sum = -inf
sum = -inf
for j = 1 to n
    currentHigh = j
    if sum > 0
        sum = sum + A[j]
    else
        currentLow = j
        sum = A[j]
    
    if sum > max_sum 
        max_sum = sum
        low = currentLow
        high = currentHigh

return (low, high, max_sum)
"""

def iterative_find_max_subarray(A):
    n = len(A)
    max_sum = -float("inf")
    sum = -float("inf")
    for j in range(n):
        currentHigh = j
        if sum > 0:
            sum += A[j]
        else:
            currentLow = j
            sum = A[j]
        
        if sum > max_sum:
            max_sum = sum
            low = currentLow
            high = currentHigh
        print(j, ":", low, high, max_sum, currentLow, currentHigh, sum)
    
    return (low, high, max_sum)

if __name__ == "__main__":
    A = [4, 2, -9, 4, 2, -1, 2]
    (low, high, max_sum) = iterative_find_max_subarray(A)
    print("=" * 30)
    print(A)
    print(low, "to", high, "with sum", max_sum)