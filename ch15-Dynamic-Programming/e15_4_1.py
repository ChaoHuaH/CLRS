# Determine an LCS of (1,0,0,1,0,1,0,1) and (0,1,0,1,1,0,1,1,0)


def lcs_length(X, Y):
    m = len(X)
    n = len(Y)
    c = [[0 for j in range(n + 1)] for i in range(m + 1)]
    b = [['x' for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = '*'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = '^'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = '<'
    return (b, c)

def print_lcs(b, X, i , j):
    if i == 0 or j == 0:
        return
    elif b[i][j] == '*':
        print_lcs(b, X, i - 1, j - 1)
        print(X[i - 1])
    elif b[i][j] == '^':
        print_lcs(b, X, i - 1, j)
    else:
        print_lcs(b, X, i, j - 1)

if __name__ == "__main__":
    X = [1,0,0,1,0,1,0,1]
    Y = [0,1,0,1,1,0,1,1,0]
    # X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    # Y = ['B', 'D', 'C', 'A', 'B', 'A']
    b, c = lcs_length(X, Y)
    # print(b)
    print_lcs(b, X, len(X), len(Y))
