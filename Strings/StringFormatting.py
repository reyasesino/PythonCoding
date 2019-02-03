def print_formatted(number):
    w = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(w, ' '), str(oct(i)[2:]).rjust(w, ' '), str(hex(i)[2:].upper()).rjust(w, ' '),str(bin(i)[2:]).rjust(w, ' '), sep=' ')
       # print(i+1 ,  oct(i+1)[2:].rjust(w, " "), (hex(i+1)).upper()[2:].rjust(w," "), bin(i+1)[2:].rjust(w," "), sep=" ")

if __name__ == '__main__':
    """"
    ####################################################################################################################
    Given an integer, , print the following values for each integer  from  to :
    Decimal
    Octal
    Hexadecimal (capitalized)
    Binary
    The four values must be printed on a single line in the order specified above for each  from  to . Each value should
    be space-padded to match the width of the binary value of .
    ####################################################################################################################
    """

    n = int(input())
    print_formatted(n)