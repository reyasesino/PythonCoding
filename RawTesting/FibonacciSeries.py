def main(upperLimit):
    results = []
    a, b = 0,1
    for i in range(upperLimit):
        results.append(a)
        a, b = b, a+b

    print(results)

def appending(a, L = {}):
    L['id'] = a
    return L

if __name__ == '__main__':
    main(10)
    main(3)
    st = ""
    st +=str(appending(2)) + "\n"
    st +=str(appending(3)) + "\n"
    print(st)