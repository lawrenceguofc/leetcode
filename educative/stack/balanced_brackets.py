from stack import Stack

def is_match(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == "}":
        return True
    elif p1 == '[' and p2 == ']':
        return True
    else:
        return False

def is_bracket_balanced(str):
    s = Stack()
    i = 0 
    is_balanced = True

    while i < len(str):
        if str[i] in '([{':
            s.push(str[i])
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop() 
                if not is_match(top,str[i]):
                    is_balanced = False 
        i += 1

    return is_balanced

    
def main():
    print("String : (((({})))) Balanced or not?")
    print(is_bracket_balanced("(((({}))))"))

    print("String : [][]]] Balanced or not?")
    print(is_bracket_balanced("[][]]]"))

    print("String : [][] Balanced or not?")
    print(is_bracket_balanced("[][]"))

if __name__ == "__main__":
    main()