# Check whether a given string contains alphanumeric characters, alphabets, digits, lowercase, and uppercase characters.
# Print the result as True or False for each condition.
if __name__ == '__main__':
    s = input()
    f1=f2=f3=f4=f5=False
    for i in s:
        f1=f1|(i.isalnum()) 
        f2=f2|(i.isalpha())
        f3=f3|(i.isdigit())
        f4=f4|(i.islower())
        f5=f5|(i.isupper())
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
