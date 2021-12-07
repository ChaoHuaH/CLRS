# Consider the problem of adding two n-bit binary integers, 
# stored in two n-element arrays A and B. 
# The sum of the two integers should be stored in 
# binary form in an (n + 1)-element array C. 
# State the problem formally and write pseudocode for adding the two integers

# Input: 
# An array of booleans A = [a1, a2, ..., an] and 
# an array of booleans B = [b1, b2, ..., bn], 
# each represent an integer stored in binary format (digit be only 0 or 1)
# and each of length n
# Output: 
# An array of booleans C = [c1, c2, ..., cn+1] 
# such that C = A + B, is the integer stored in binary format

"""
// ADD-BINARY(A, B)
C = new integer[A.length + 1]
carry = 0
for i = A.length downto 1
    C[i + 1] = (A[i] = B[i] + carry) % 2 // reminder
    carry =  (A[i] = B[i] + carry) / 2   // quotient
    i -= 1
C[1] = carry
"""

A = [1, 0, 1, 0, 1, 1, 0, 1]
B = [0, 1, 1, 1, 0, 1, 1, 1]
C = [0] * (len(A) + 1)
carry = 0
for i in range(len(A)-1, -1, -1):
    C[i + 1] = (A[i] + B[i] + carry) % 2
    carry = (A[i] + B[i] + carry) // 2
    i -= 1
C[0] = carry
print("A:   ", A)
print("B:   ", B)
print("C:", C)