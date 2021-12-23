# Write pseudocode for the brute-force method of 
# solving the maximum-subarray problem. Your procedure should run in Theta(n^2) time.

"""
// BRUTE-FORCE-FIND-MAXIMUM-SUBARRAY(A)
n = A.length
max-sum = -inf
low = -inf
high = -inf
for i = 1 to n                 // n times
    sum = 0
    for j = i to n             // Theta(n)
        sum += A[j]
        if sum > max-sum
            max-sum = sum
            low = i
            high = j
return (low, high, max-sum)
"""

def bruteFindMaxSeq(A):
    n = len(A)
    max_sum = -float("inf")
    low = -float("inf")
    high = -float("inf")
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
                low = i
                high = j
    return (low, high, max_sum)

if __name__ == "__main__":
    A = [8, -4, 3, -4, 4, 5, 1]
    [a, b, c] = bruteFindMaxSeq(A)
    print("start:", a)
    print("  end:", b)
    print("  sum:", c)
