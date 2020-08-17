
from stack import Stack

def int_to_bin(num):
    s = Stack()
    while num > 0:
        remainder = num % 2
        s.push(remainder)
        num  = num // 2
    print(s.get_stack())
    output = 0
    while len(s.get_stack()) > 0:
        length = len(s.get_stack())
        var = s.pop()
        output += var * (10 ** (length - 1))
    return output


def main():
    print(int_to_bin(242))

if __name__ == "__main__":
    main()
