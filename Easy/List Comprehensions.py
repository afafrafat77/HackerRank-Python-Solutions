# Generate all possible 3D coordinates within a cuboid and filter out those whose sum equals a given integer.
# Use list comprehension to create and print the valid coordinates in lexicographic order, excluding sums that match the given integer.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k!=n)]
    print(l)       
