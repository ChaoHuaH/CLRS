# Referring back to the searching problem (see Exercise 2.1-3), 
# observe that if the sequence A is sorted, 
# we can check the midpoint of the sequence against v 
# and eliminate half of the sequence from further consideration. 
# The binary search algorithm repeats this procedure, 
# halving the size of the remaining portion of the sequence each time. 
# Write pseudocode, either iterative or recursive, for binary search. 
# Argue that the worst-case running time of binary search is Theta(lg(n)).

"""
// ITERATIVE-BINARY-SEARCH(A, v)
idx_start = 1
idx_end = A.length
if v < A[idx_start] or v > A[idx_end]
    return NIL
while idx_start <= idx_end:
    idx_mid = (idx_end + idx_start) // 2
    if v = A[idx_mid]:
        return mid_idx
    elif v < A[idx_mid]:
        idx_end = idx_mid - 1
    else:
        idx_start = idx_mid + 1
return NIL
"""

def iterBinarySerach(A, v):
    idx_start = 0
    idx_end = len(A) - 1
    if v < A[idx_start] or v > A[idx_end]:
        return None
    while idx_start <= idx_end:
        idx_mid = (idx_start + idx_end) // 2
        if v == A[idx_mid]:
            return idx_mid
        elif v < A[idx_mid]:
            idx_end = idx_mid - 1
        else:
            idx_start = idx_mid + 1
    return None

"""
// RECURSIVE-BINARY-SEARCH(A, v, low, high)
if low > high
    return NIL
mid = (low + high) // 2
if v == A[mid]
    return mid
elif v < A[mid]
    return RECURSIVE-BINARY-SEARCH(A, v, low, mid - 1)
else
    return RECURSIVE-BINARY-SEARCH(A, v, mid + 1, high)
"""

def recurBinarySerach(A, v, low, high):
    if low > high:
        return None
    mid = (low + high) // 2
    if v == A[mid]:
        return mid
    elif v < A[mid]:
        return recurBinarySerach(A, v, low, mid - 1)
    else:
        return recurBinarySerach(A, v, mid + 1, high)

if __name__ == "__main__":    
    A = [26, 31, 41, 58, 59, 89]
    v = 58
    print(A)
    print("v:", v)
    print("iterative:", iterBinarySerach(A, v))
    print("recursive:", recurBinarySerach(A, v, 0, len(A) - 1))

# T(n) = Theta(1)           if n = 1
# T(n) = 2T(n/2) + Theta(1) if n > 1
# >>> T(n) = Theta(lg n)