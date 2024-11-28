# Create a door mat design based on the given dimensions with 'WELCOME' at the center.
# The design should use the specified characters (.|-) and be symmetrical around the center.
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    N, M = map(int, input().split())
    for i in range(1,N,2):
         print (('.|.'*i).center(M,'-'))
    print ('WELCOME'.center(M,'-'))
    for i in range(N-2,-1,-2):
         print (('.|.'*i).center(M,'-'))
