# Create a tuple from the given space-separated integers.
# Compute and print the hash of the tuple using the built-in hash() function.
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)
    print(hash((t)))
    
