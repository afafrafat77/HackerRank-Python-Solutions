# Given a string, modify the character at a specific index with a new character.
# Return the modified string after the change is made at the specified position.
def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string = ''.join(l)
    return string
