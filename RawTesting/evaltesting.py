def main():
    x = 3
    y = "x*3+x*3"
    z = eval(y)
    print(z)




if __name__ == '__main__':
    safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']

    # creating a dictionary of safe methods
    safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])
    print(safe_dict)
    main()