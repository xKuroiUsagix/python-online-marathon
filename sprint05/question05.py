import cmath


def solve_quadric_equation(a, b, c):
    try:
        D = cmath.sqrt(float(b)**2 - 4*float(a)*float(c))
        x1 = (-float(b) - D) / (2 * float(a))
        x2 = (-float(b) + D) / (2 * float(a))
        return f'The solution are x1={x1} and x2={x2}'
    except ValueError:
        return 'Could not convert string to float'
    except ZeroDivisionError:
        return 'Zero Division Error'