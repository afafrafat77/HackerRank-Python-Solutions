# Convert a given complex number to polar coordinates by calculating its modulus and phase angle.
# Use cmath's abs() and phase() functions to extract the modulus and phase, respectively.
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
n = input()
s = complex(n)
print(abs(s))
print(cmath.phase(s))
