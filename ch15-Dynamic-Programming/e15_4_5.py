# Give an O(n^2)-time algorithm to find 
# the longest monotonically increasing subsequence of a sequence of n numbers.

import e15_4_1

"""
// LONGEST-INCREASE-SUB(X)
// let Y be a new sequence of monotonically increasing sort X  (Theta(n lg n) = o(n^2))
// the longest common sequence of X and Y
// is longest monontonically increasing subsequence of X
"""
def longest_increase_sub(X):
    n = len(X)
    Y = sorted(X)
    print(X)
    # print(Y)
    b, c = e15_4_1.lcs_length(X, Y)
    e15_4_1.print_lcs(b, X, n, n)

if __name__ == "__main__":
    X = [2, 2, 4, 7, 1, 9, 6, 8, 5, 10, 3, 2]
    longest_increase_sub(X)
