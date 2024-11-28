# Kevin and Stuart play a game where they form substrings starting with vowels and consonants, respectively.
# The player scores points based on the frequency of each substring in the given string, and the winner is determined by their total score.

def minion_game(string):
    k=0
    s=0
    for i in range(len(string)):
        l=len(string)-i
        if string[i] in 'AEIOU':
            k+=l
        else:
            s+=l    
    if k>s:
        print(f"Kevin {k}")
    elif k<s:
        print(f"Stuart {s}")
    else:
        print("Draw")
__name__
if __name__ == '__main__':
    s = input()
    minion_game(s)
