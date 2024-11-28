# Given a string and a substring, count how many times the substring appears in the string.
# The search should be case-sensitive and performed from left to right.
def count_substring(string, sub_string):
    cnt=0
    for i in range(0, len(string)):
        flag=True
        temp=i
        for j in sub_string:
            if(temp>=len(string)):
                flag=False
                break
            if(string[temp]!=j):
                flag=False
                break
            temp+=1    
        if(flag):
            cnt+=1        
    return cnt
    
