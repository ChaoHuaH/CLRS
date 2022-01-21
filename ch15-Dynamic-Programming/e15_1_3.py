# Consider a modification of the rod-cutting problem in which, 
# in addition to a price pi for each rod, each cut incurs a fixed cost of c. 
# The revenue associated with a solution is now the sum of the prices of the pieces 
# minus the costs of making the cuts. 
# Give a dynamic-programming algorithm to solve this modified problem.

def cut_rod(p, n):
    r = [0 for i in range(n + 1)]
    for j in range(1, n + 1):
        # print(j)
        q = p[j - 1]  # p[i] for i = 0, ..(n - 1) 
        for i in range(1, j):
            # print(j, i)
            new_value = p[i - 1] + r[j - i]
            # print("new:", new_value)
            if new_value > q:
                q = new_value
        r[j] = q
        print(r)
    return r[n]

"""
// MODIFIED-CUT-ROD(p, n, c)
let r[0..n] be a new array
r[0] = 0
for j = 1 to n
    q = p[j]
    for i = 1 to j - 1
        q = max(q, p[i] + r[j - i] - c)
    r[j] = q
return r[n]
"""

def modified_cut_rod(p, n, c):
    r = [0 for i in range(n + 1)]
    for j in range(1, n + 1):
        # print(j)
        q = p[j - 1]
        for i in range(1, j):
            # print(j, i)
            new_value = p[i - 1] + r[j - i] - c
            # print("new:", new_value)
            if new_value > q:
                q = new_value
        r[j] = q
        print(r)
    return r[n]

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10 ,17, 17, 20, 24, 30]
    n = 7
    c = 1
    print("\nOptimal revenue:", cut_rod(p, n))
    print("\nOptimal revenue(modified):", modified_cut_rod(p, n, c))