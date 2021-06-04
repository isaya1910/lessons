from mytest4 import Stack


def is_scopes_balance(scopes):
    stack = Stack()
    for c in scopes:
        if c == '(':
            stack.push(c)
        if c == ')':
            scope = stack.pop()
            if scope is None:
                return False
    if stack.size() > 0:
        return False
    return True


def polish_notation(notation):
    stack = Stack()
    for c in notation:
        if c.isdigit():
            stack.push(int(c))

        if c == '+':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.push(digit1 + digit2)
        if c == '-':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.push(digit1 - digit2)
        if c == '*':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.push(digit1 * digit2)
        if c == '/':
            digit1 = stack.pop()
            digit2 = stack.pop()
            stack.push(digit1 / digit2)

    return stack.pop()
