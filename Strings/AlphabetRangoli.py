def print_rangoli(size):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    gettingstarter = alphabets[size-1]
    count = 0
    stringmaking = []
    for i in range(1,size*3,2):
        stringmaking.append(chr(ord(gettingstarter)-count))
        for i in stringmaking:
            stringmaking.append(i)
        print("-".join(stringmaking).center(size*3, "-"))
        count = count+1


if __name__ == '__main__':
    #n = int(input())
    print_rangoli(3)