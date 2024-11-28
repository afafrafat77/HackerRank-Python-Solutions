# Find the runner-up score from a list of scores by determining the second highest unique score.
# Print the runner-up score after removing duplicates and sorting the list in descending order.
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    mx=-150
    mx2=-150
    for i in l:
        if(mx<i):
            mx=i
    for i in l:
        if(i!=mx and mx2<i):
            mx2=i
    print(mx2)                  
    
