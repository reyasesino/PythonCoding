def split_and_join(line):

    split = line.split(" ")
    joining = "-".join(split)
    return joining


if __name__ == '__main__':
    split_and_join(input())