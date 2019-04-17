def split_and_join(line)->str:

    split = line.split(" ")
    joining = "-".join(split)
    return joining


if __name__ == '__main__':
    print(split_and_join(input()))