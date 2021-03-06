# Consider the searching problem:
# Input: A sequence of n numbers A = [a1, a2, ..., an] and a value v.
# Output: An index i such that v = A[i] or the special value NIL if v does not appear in A.

# Write pseudocode for linear search, which scans through the sequence, 
# looking for v. Using a loop invariant, prove that your algorithm is correct. 
# Make sure that your loop invariant fulfills the three necessary properties.

"""
// LINEAR-SEARCH(A, v)
for i = 1 to A.length
    if A[i] == v
        return i
return NIL
"""

A = [31, 41, 59, 26, 41, 58]
v = 58
def linear_search(A, v):
    for i in range(len(A)):
        if A[i] == v:
            return i
    return "NA"

print("index =", linear_search(A, v))
