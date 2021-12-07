# Describe a Theta(nlg n)-time algorithm that, 
# given a set S of n integers and another integer x, 
# determines whether or not there exist two elements in S 
# whose sum is exactly x

"""
// FIND-SUM(S, x)
n = S.length
reverse sort S     // Theta(nlg n)
S2[1..n] be a new array
for i = 1 to n
        S2[i] = x - S[i] // Theta(n)
for j = 1 to n                               // n times
    k = ITERATIVE-BINARY-SEARCH(S2, S[j])    // Theta(lg n)
    if k is not None:
        print(S[j], S[k])
        return 1
return 0
// Theta(nlg n) + Theta(n) + n*Theta(lg n) = Theta(nlg n)
"""

from e2_3_5 import iterBinarySerach

def findSum(S, x):
    n = len(S)
    S.sort(reverse = True)
    S2 = [0] * n
    for i in range(n):
            S2[i] = x - S[i]
    print(S)
    print(S2)
    for j in range(n):
        k = iterBinarySerach(S2, S[j])
        if k is not None:
            print(S[j], S[k])
            return True
    return False

if __name__ == "__main__":
    # S = [10, 30, 1, 2, 3, 4, 5]
    S = [5, 4, 3, 2, 1]
    print(findSum(S, 6))
    
    



