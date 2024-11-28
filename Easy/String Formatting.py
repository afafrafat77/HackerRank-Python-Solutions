# Print the decimal, octal, hexadecimal (capitalized), and binary values for each integer 
# from 1 to the given number, with values space-padded to match the width of the binary value.
def print_formatted(number):
    # your code goes here
    w = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(str(i).rjust(w),oct(i)[2:].rjust(w),hex(i)[2:].upper().rjust(w),bin(i)[2:].rjust(w))
