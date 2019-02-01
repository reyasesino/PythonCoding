import textwrap

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(max_width)
    wrapper_list = wrapper.wrap(string)
    return '\n'.join(wrapper_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)