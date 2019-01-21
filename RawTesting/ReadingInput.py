def main(value):
   for _ in range(value):
       s = map(int,input().split())
       tset = tuple(s)
       print(hash(tset))


if __name__ == '__main__':
    main(int(input()))