# Find and print the names of students with the second lowest grade, sorted alphabetically.
# Ensure the output includes only the students with the second unique lowest grade.
if __name__ == '__main__':
    l=[]
    mn=1000
    mn2=1000
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x=[name,score]
        l.append(x)
        if score <mn:
            mn=score
    sort = sorted(l)        
    for i,j in l:
        if(j!=mn and j<mn2):
            mn2=j
    s=set() 
    for i,j in sort:
        if(j==mn2):
            print(i)                               
        
