# Modify MEMOIZED-CUT-ROD to return not only the value 
# but the actual solution, too.

def memory_cut_rod(p, n):
    r = [-float("inf") for i in range(n + 1)]
    return memory_cut_rod_aux(p, n, r)

def memory_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n + 1):
            new_value = p[i - 1] + memory_cut_rod_aux(p, n - i, r)
            if new_value > q:
                q = new_value
    r[n] = q
    return q

"""
// MODIFIED-MEMORY-CUT-ROD(p, n)
let r[0..n] and s[0..n] be new arrays
for i = 0 to n
    r[i] = -inf
    s[i] = i
(val, s) = MODIFIED-MEMORY-CUT-ROD-AUX(p, n, r, s)
while n > 0
    print(s[n])
    n = n - s[n]

// MODIFIED-MEMORY-CUT-ROD-AUX(p, n, r, s)
if r[n] >= 0
    return (r[n], s)
if n == 0
    q = 0
else
    q = -inf
    for i = 1 to n
        (val, s) = MODIFIED-MEMORY-CUT-ROD-AUX(p, n - i, r, s)
        if q <  p[i] + val
            q = p[i] + val
            s[n] = i
r[n] = q
return (q, s)
"""

def md_memory_cut_rod(p, n):
    r = [-float("inf") for i in range(n + 1)]
    s = [i for i in range(n + 1)]
    val, s = md_memory_cut_rod_aux(p, n, r, s)
    print("Optimal value:", val)
    while n > 0:
        print(s[n])
        n = n - s[n]

def md_memory_cut_rod_aux(p, n, r, s):
    if r[n] >= 0:
        return (r[n], s)
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(1, n + 1):
            val, s = md_memory_cut_rod_aux(p, n - i, r, s)
            if q < p[i - 1] + val:
                q = p[i - 1] + val
                s[n] = i
    r[n] = q
    return (q, s)


if __name__ == "__main__":
    p = [1, 5, 8, 9, 10 ,17, 17, 20, 24, 30]
    n = 9
    c = 1
    # print("Optimal revenue:", memory_cut_rod(p, n))
    for i in range(1, 11):
        print("======")
        print("n:", i)
        md_memory_cut_rod(p, i)

    