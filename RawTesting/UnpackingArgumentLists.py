def main(*args):
    print(list(range(*args)))

def testing(id, value, name, marks):
    print(" A has id {} and value {} with name {} and marks {}".format(id, value, name, marks))

if __name__ == '__main__':
    main(int(input("Enter Upper Limit :: ")), int(input("Enter Lower Limit:: ")))
    dictionar = {
        "id" : 10,
        "value" : 20,
        "name" : "cool",
        "marks" : 2000,
        "age" : 20
    }
    testing(**dictionar)