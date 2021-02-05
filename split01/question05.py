def toPostFixExpression(expression: list) -> list:
    operators = ['-', '+', '*', '/', '%']
    open_p, close_p = '(', ')'
    output = []
    output_operators = []

    for number in expression:
        if number not in operators:
            output.append(number)
        else:
            output_operators.append(number)

    return output + output_operators


print(toPostFixExpression(['2', '+', '3']))
# 20 + 3 * (5 * 4) = 20 3 5 4 * * +
# 
