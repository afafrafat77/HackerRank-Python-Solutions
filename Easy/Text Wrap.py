# Wrap a given string into lines of a specified width, inserting newline characters where necessary.
# The resulting string should have lines that do not exceed the given width.


def wrap(string, max_width):
    k=""
    for i in range (len(string)):
        if(i%max_width==0 and i!=0):
            k+=('\n')
        k+=string[i]    
            
    return k
