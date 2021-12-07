# Consider sorting n numbers stored in array A 
# by first finding the smallest element of A and exchanging it with the element in A[1]. 
# Then find the second smallest element of A, and exchange it with A[2]. 
# Continue in this manner for the first n - 1 elements of A. 
# 
# Write pseudocode for this algorithm, which is known as selection sort. 

"""
// SELECTION-SORT(A)
for i = 1 to (A.length - 1)
    min_idx = i
    for j = i + 1 to A.length 
        if A[j] < A[min_idx]
            min_idx = j
    swap(A[i], A[min_idx])
"""

A = [5, 22, 1, 9, 3, 4, 10, 4]
print("Original:", A, "\n")
def selection_sort(A):
    for i in range(len(A) - 2):
        min_idx = i
        j = i + 1
        while j < len(A):
            if A[j] < A[min_idx]:
                min_idx = j
            j += 1
        min_value = A[min_idx]
        A[min_idx] = A[i]
        A[i] = min_value
        print(i, ": ", A, sep = "")
    return A
print("\nFinal:", selection_sort(A))

# What loop invariant does this algorithm maintain? 

# Why does it need to run for only the first n - 1 elements, 
# rather than for all n elements? 
# Anser: after sorting the prior n-1 elements, the n element already the biggest number

# Give the best-case and worst-case running times of selection sort in theta-notation
# Both theta(n^2)