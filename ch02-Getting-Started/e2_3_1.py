# Using Figure 2.4 as a model, 
# illustrate the operation of merge sort on the array 
# A = [3,41,52,26,38,57,9,49]

# p, q, and r are index start from 0
def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0 for i in range(n1 + 1)]
    R = [0 for j in range(n2 + 1)]
    for i in range(n1):
        L[i] = A[p + i]
    L[-1] = float('inf')
    for j in range(n2):
        R[j] = A[q + 1 + j]
    R[-1] = float('inf')
    print(L, ":", R)

    i = 0
    j = 0
    k = p
    for k in range(p, r + 1): 
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    print(A)
    print('=' * 50) 

def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)
    return A

if __name__ == "__main__":
    A = [3,41,52,26,38,57,9,49]
    # A = [4, 2, 8, 1, 6, 5, 3, 7]
    output = mergeSort(A, 0, 7)
    print("final:", output)
