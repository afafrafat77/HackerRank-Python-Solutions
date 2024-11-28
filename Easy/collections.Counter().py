# Calculate the total money earned by a shoe shop owner based on customers' shoe size requests and prices.
# Use collections.Counter to track available shoe sizes and ensure customers only purchase if the size is available.
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
N=int(input())
L=map(int,input().split())
M=int(input())
C=Counter(L)
x=list()
sum=0
for i in range(M):
    temp = input().split(" ")
    if(C[int(temp[0])]>0):
        sum+=int(temp[1])
        C[int(temp[0])]-=1
print(sum)        
           
