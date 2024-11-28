# This function splits the string into substrings of length k and removes duplicate characters from each substring.
# It prints each resulting substring, preserving the order of first occurrences of characters.
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        s=string[i:i+k]
        s=''.join(set(s))
        print(s)
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
