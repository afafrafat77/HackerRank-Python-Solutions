# Check if a given integer is "Weird" or "Not Weird" based on specific conditions of odd/even and ranges.
# Print "Weird" for odd numbers or specific even ranges; otherwise, print "Not Weird".
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        print("Weird")
    elif(n>=2 and n<=5):
        print("Not Weird")
    elif(n>=6 and n<=20):
        print("Weird") 
    else:   
        print("Not Weird")      
