
import math
import os
import random
import re
import sys

def main(n,ar):
    dictionay = dict((x, ar.count(x)) for x in set(ar))
    for x in set(ar):
        print(x, ar.count(x))
    sum = 0
    for i in dictionay:
        sum = sum + math.floor(dictionay[i]/2)
    return sum

if __name__ == '__main__':
    #print(os.environ)

    #fptr = open(os.environ['PYTHONPATH'], 'w')
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #ar = list(map(int, input().rstrip().split()))

    result = main(5, [10 ,20 ,20, 10, 10, 30, 50 ,10 ,20])
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
