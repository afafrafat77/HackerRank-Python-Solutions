# Calculate and print the average marks of a specific student, rounded to two decimal places.
# The student's marks are retrieved from a dictionary based on the provided name.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    for i in  student_marks[query_name]:
        sum+=i
    print(f'{sum/len(student_marks[query_name]):.2f}')    
