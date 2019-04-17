import sys

def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")





if __name__ == '__main__':
    #print(repeatedString("aba",10))
    print(repeatedString('a',1000000000000))