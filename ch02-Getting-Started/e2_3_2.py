# Rewrite the MERGE procedure so that it does not use sentinels, 
# instead stopping once either array L or R has had all its elements copied back to A 
# and then copying the remainder of the other array back into A.

"""
// MERGE(A, p, q, r)
n1 = q - p + 1
n2 = r - q
Let L[1...n1] and R[1...n2] be new arrays
for i = 1 to n1
    L[i] = A[p + i - 1]
for j = 1 to n2
    R[j] = A[q + j]

i = 1
j = 1
k = p
while i <= n1 and j <= n2
    if L[i] <= R[j]
        A[k] = L[i]
        i += 1
    else
        A[k] = R[j]
        j += 1
    k += 1

for m = k to r
    if i < n1
        A[m] = L[i]
        i += 1
    else 
        A[k] = L[i]
        j += 1
"""

def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0 for i in range(n1)]
    R = [0 for j in range(n2)]
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + 1 + j]
    print(L, ":", R)

    i = 0
    j = 0
    k = p
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        # print(A)
    
    for m in range(k, r + 1):
        if i < n1:
            A[m] = L[i]
            i += 1
        else:
            A[m] = R[j]
            j += 1
    
    print(A)
    print('=' * 50)


def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
    return A


# A = [3,41,52,26,38,57,9,49]
A = [4, 2, 8, 1, 6, 5, 3, 7]
output = mergeSort(A, 0, 7)
print("final:", output)