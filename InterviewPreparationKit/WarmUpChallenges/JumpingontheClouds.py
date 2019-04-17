def main(n, c):
    step =0;
    # Doing with the help of the stack :
    countingzeros = 0
    arr = []
    pointer = 0
    for i in c:
        if(i == 0):
            arr.append(i)
            pointer = pointer + 1
            if(pointer == 3):
                arr.pop()
                pointer = 1
        else:
            pointer = 0

    return len(arr)-1

if __name__ == '__main__':
    print(main(7, [0,0,1,0,0,1,0]) == 4)
    print(main(6, [0, 0, 0, 0, 1, 0]) == 3)
    print(main(6, [0,0,0,1,0,0]) == 3)
    print(main(7, [0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 , 1, 0, 1, 0, 0]))