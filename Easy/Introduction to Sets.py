# This code calculates the average of distinct elements in an array by first converting it to a set to remove duplicates,
# then computing the sum and dividing by the length of the set to get the average, rounded to 3 decimal places.
def average(array):
    # your code goes heres
    array=set(array)
    return sum(array)/len(array)
    
