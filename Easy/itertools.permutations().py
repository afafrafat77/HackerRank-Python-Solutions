# Print all possible permutations of a given string of specified length in lexicographic sorted order.
# Use itertools.permutations to generate permutations and print them on separate lines.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, n = input().split()
for i in sorted(permutations(s,int(n))):
    print (''.join(i))
