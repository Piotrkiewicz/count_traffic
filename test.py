

def convert_to_str(x):
    return str(x) + ' courtesy of string converted'


def print_string(s):
    print('printing string:')
    print(s)


def do_two_things():
    x = 7
    xs = convert_to_str(x)
    print_string(xs)


if __name__ == "__main__":
    x = 5

    x += 5

    do_two_things()
    # print(x)