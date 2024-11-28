# Given a string of space-separated words, split the string by spaces and join the words using a hyphen.
# Return the resulting string after splitting and joining.


def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
