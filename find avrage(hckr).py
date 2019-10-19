if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        #student_marks[average]=sum(scores)/3
    query_name = input()
    result = student_marks[query_name]
    print("{0:.2f}".format(sum(result)/3))
