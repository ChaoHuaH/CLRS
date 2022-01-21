# The Fibonacci numbers are defined by recurrence (3.22). 
# Give an O(n)-time dynamic-programming algorithm to compute the nth Fibonacci number. 
# Draw the subproblem graph. How many vertices and edges are in the graph?

"""
// FIBONACCI(n)
let fib[0...n] be a new array
fib = [0 for i = 0 to n]
fib[0] = 0
fib[1] = 1
for i = 2 to n
    fib[i] = fib[i - 1] + fib[i - 2]
return fib[n]
"""

def fibonacci(n):
    fib = [0 for i in range(n + 1)]
    if n <= 1:
        return n
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

if __name__ == "__main__":
    for i in range(21):
        print("n =", '{0:2}'.format(i), ":", fibonacci(i))