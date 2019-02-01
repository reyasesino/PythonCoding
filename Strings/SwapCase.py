def swapcase(reader):
    conversion = []
    for i in reader:
        if i.islower():
            conversion.append(i.upper())
        elif i.isupper():
            conversion.append(i.lower())
        else:
            break

    str1 = ''.join(conversion)

    print(reader.swapcase())
    print(str1)


if __name__ == '__main__':
   swapcase(input())