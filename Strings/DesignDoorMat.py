def main(row, column):
    cen = ".|."
    for i in range(1,row,2):
        print((cen * (i)).center(column, "-"))
    str = "WELCOME"
    print(str.center(column,"-"))

    for i in range(row-2,0, -2):
        print((cen * (i)).center(column, "-"))


if __name__ == '__main__':
    inte = input()
    dim = inte.split(" ")
    main(int(dim[0]), int(dim[1]))