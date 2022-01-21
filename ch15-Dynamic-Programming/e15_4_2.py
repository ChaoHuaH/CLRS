# Give pseudocode to reconstruct an LCS from the completed c table 
# and the original sequences X = [x2, x2, ..., xm] and Y = [y1, y2, ..., yn] 
# in O(m + n) time, without using the b table.

from e15_4_1 import lcs_length

"""
// PRINT-LCS2(c, X, Y, i, j)
if c[i][j] == 0
    return
if X[i] = Y[j]:
    PRINT-LCS2(c, X, Y, i - 1, j - 1)
    print xi
elseif c[i - 1][j] >= c[i][j - 1]
    PRINT-LCS2(c, X, Y, i - 1, j)
else
    PRINT-LCS2(x, X, Y, i, j - 1)
"""

def print_lcs2(c, X, Y, i, j):
    if c[i][j] == 0:
        return
    if X[i - 1] == Y[j - 1]:
        print_lcs2(c, X, Y, i - 1, j -1)
        print(X[i - 1])
    elif c[i - 1][j] >= c[i][j - 1]:
        print_lcs2(c, X, Y, i - 1, j)
    else:
        print_lcs2(c, X, Y, i, j -1)

if __name__ == "__main__":
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    b, c = lcs_length(X, Y)
    print(c)
    print_lcs2(c, X, Y, len(X), len(Y))
