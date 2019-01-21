




if __name__ == '__main__':
    students = []
    max = 0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        if(score < max):
            min = score

    for i in students:
        if i[1] == min:
            students.remove(i)

    min = students[0][1]
    for i in students:
        #print(i[1])
        if i[1] == min:
            min = i[1]

    finallist =[]
    for i in students:
        if i[1]== min:
            finallist.append(i)


    finallist.sort()
    for i in finallist:
        print(i[0])