# Show how to compute the length of an LCS using only 2*min(m, n) entries in the c table 
# plus O(1) additional space. Then show how to do the same thing, but using
# min(m, n) entries plus O(1) additional space.

"""
// SMALL-SPACE-LCS-LENGTH(X, Y)
// to use 2min(m, n) space, the second loop should be the shorter one
// we assume Y is the shorter one
m = X.length
n = Y.length
let c[0..1, 0...n] be a new table
for j = 0 to n
    c[0, j] = 0
c[1, 0] = 0

for i = 1 to m
    for j = 0 to n  # shorter len variables
        if X[i] == Y[j]
            c[1, j] = c[0, j - 1] + 1
        elseif c[0, j] >= c[1, j - 1]
            c[1, j] = c[0, j]
        else
            c[1, j] = c[1, j -1]
    for j = 0 to n
        c[0, j] = c[1, j]
        c[1, j] = 0
    i += 1
return max(c)
"""

def small_lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for j in range(n + 1)] for i in range(2)]

    for i in range(1, m + 1):
        print(c)
        for j in range(n + 1):
            c[0][j] = c[1][j]
            c[1][j] = 0

        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                c[1][j] = c[0][j - 1] + 1
            elif c[0][j] >= c[1][j - 1]:
                c[1][j] = c[0][j]
            else:
                c[1][j] = c[1][j - 1]
        i += 1
    print(c)
    print("LCS-length:", max(c[1]))

"""
// to use only min(m, n) space
// we only need c[i - 1, j - 1], c[i, j - 1], c[i - 1, j] to calculate the length
// when go to element c[i, j], free c[i - 1, j - 2]
"""

if __name__ == "__main__":
    X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    Y = ['B', 'D', 'C', 'A', 'B', 'A']
    small_lcs_length(X, Y)