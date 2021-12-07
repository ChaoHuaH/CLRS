# Rewrite the INSERTION-SORT procedure to sort into nonincreasing 
# instead of nondecreasing order.

"""
// INSERTION-SORT(A, reverse)
for j = 2 to A.length
    key = A[j]
    i = j - 1
    while i > 0 and A[i] < key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
"""

A = [31, 41, 59, 26, 41, 58]
print("0:", A)
for j in range(1, len(A)):
    key = A[j]
    i = j - 1
    while i >= 0 and A[i] < key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key
    print(j, ": ", A, sep = "")