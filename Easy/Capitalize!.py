# Given a full name, capitalize the first letter of each word while keeping the rest lowercase.
# The solution ensures that names like 'chris alan' are formatted as 'Chris Alan'.


# Complete the solve function below.
def solve(s):
    s = s.split(" ")
    for i in range(len(s)):
        if s[i] and s[i][0].islower(): 
            s[i] = s[i][0].upper() + s[i][1:]
    s = ' '.join(s)  
    return s       
