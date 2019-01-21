"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.


"""
from datetime import datetime


def main(total, arr):
    t1 = datetime.now()
    arr.sort()
    for i in range(total-1, 0, -1):
        if arr[i] != arr[i-1]:
            l = arr[i-1]
            break
        else:
            arr.pop()
    t2 = datetime.now()

    print(t2-t1)
    print(l)


def main2(total, arr):
    t1 = datetime.now()
    maxvalue = max(arr)
    for i in arr:
        if i == maxvalue:
            arr.remove(maxvalue)
    print(max(arr))
    t2 = datetime.now()
    print((t2-t1)*10000000)
    return max(arr)


if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    main(N, arr)
    main2(N, arr)
