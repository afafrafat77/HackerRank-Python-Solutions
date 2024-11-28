# Print a sequence of integers from 1 to n as a single string without spaces.
# The output should be the concatenation of all numbers from 1 to n, without using string methods.
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end="")
        
