# Given an integer 'size', print an alphabet rangoli of the given size with letters 'a' to the corresponding letter.
# The rangoli is symmetric, with each line containing alphabets separated by hyphens and centered within the pattern.
def print_rangoli(size):
    # your code goes here
    width=size+3*(size-1)
    letters = [chr(ord('a') + i) for i in range(n)]
    for i in range(size-1,0,-1):
        l='-'.join(letters[n-1:i:-1])+'-' if i != size - 1 else ''
        r='-'.join(letters[i:n])
        print((l+r).center(width,'-'))
        
    for i in range(size):
        l='-'.join(letters[n-1:i:-1])+'-' if i != size - 1 else ''
        r='-'.join(letters[i:n])
        print((l+r).center(width,'-'))
        
