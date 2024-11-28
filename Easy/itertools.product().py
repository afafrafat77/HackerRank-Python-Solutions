# Given two lists, compute their cartesian product using itertools.product().
# The result is printed as space-separated tuples in sorted order.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in list(product(A, B)):
    print(i,end=" ") 
