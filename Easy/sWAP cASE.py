# Given a string, swap the case of each letter (lowercase to uppercase and vice versa).
# Return the modified string with all letters' cases swapped.
def swap_case(s):
    k=''
    for i in range(len(s)):
        if s[i].islower():
            k+=s[i].upper()
        elif s[i].isupper():
            k+=s[i].lower()
        else:
             k+=s[i]
    return k
