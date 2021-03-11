def toPostFixExpression(expression: list) -> list:
    operators = {'+': 0, '-': 0, '*': 1, '/': 1, '%': 1}
    open_p, close_p = '(', ')'
    postfix = []
    stack = []

    for i in expression:
        try:
            if i not in operators.keys() and i not in [open_p, close_p]:
                postfix.append(i)
            elif operators.get(stack[-1], -1) < operators.get(i, -1) or stack[-1] == open_p:
                stack.append(i)
            else:
                while len(stack) and operators.get(stack[-1]) >= operators.get(i, 2)\
                                and stack[-1] not in [open_p, close_p]:
                    postfix.append(stack.pop())
                stack.append(i)
        except IndexError:
            stack.append(i)
            continue

        if i == close_p:
            while len(stack) and stack[-1] != '(':
                if stack[-1] in [open_p, close_p]:
                    stack.pop()
                else:
                    postfix.append(stack.pop())
            stack.pop()

    while len(stack):
        postfix.append(stack.pop())

    return postfix


print(toPostFixExpression(["20",
                           "+",
                           "3",
                           "*",
                           "(",
                           "5",
                           "*",
                           "4",
                           ")"]))
