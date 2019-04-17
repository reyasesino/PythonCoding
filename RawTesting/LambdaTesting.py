def my_funtion( number : int) -> int:
    y : int = 10
    print(y)
    return lambda x : x + number




if __name__ == '__main__':
    print(my_funtion(10)(10.0))

