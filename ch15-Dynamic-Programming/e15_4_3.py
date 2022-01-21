# Give a memoized version of LCS-LENGTH that runs in O(mn) time

from e15_4_2 import print_lcs2

"""
// MEMOIZED-LCS-LENGTH(X, Y, i, j)
if c[i][j] > -1
    return c[i][j]
if i == 0 or j == 0
    return c[i][j] = 0
if X[i] == Y[j]
    return c[i][j] = MEMOIZED-LCS-LENGTH(X, Y, i-1, j-1) + 1
return c[i, j] = max(MEMOIZED-LCS-LENGTH(X, Y, i-1, j), MEMOIZED-LCS-LENGTH(X, Y, i, j-1))
"""

def memoized_lcs_length(c, X, Y, i, j):
    if c[i][j] > -1:
        return c[i][j]
    if i == 0 or j == 0:
        c[i][j] = 0
        return c[i][j]
    if X[i - 1] == Y[j - 1]:
        c[i][j] = memoized_lcs_length(c, X, Y, i - 1, j - 1) + 1
        return c[i][j]
    left = memoized_lcs_length(c, X, Y, i, j - 1)
    up   = memoized_lcs_length(c, X, Y, i - 1, j)
    if left > up:
        c[i][j] = left
    else:
        c[i][j] = up
    return c[i][j]

if __name__ == "__main__":
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    c = [[-1 for j in range(len(Y) + 1)] for i in range(len(X) + 1)]
    memoized_lcs_length(c, X, Y, len(X), len(Y))
    print(c)
    print_lcs2(c, X, Y, len(X), len(Y))
