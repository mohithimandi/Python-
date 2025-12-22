if __name__ == '__main__':
    students = []
    
    n = int(input())
    
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    scores = sorted(set(student[1] for student in students))

    second_lowest = scores[1]

    names = [student[0] for student in students if student[1] == second_lowest]

    names.sort()

    for name in names:
        print(name)