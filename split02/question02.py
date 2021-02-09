from math import fabs


def morse_number(number: str) -> str:
    get_code = lambda num, code: num * code 
    morse_code = ''
    for i in number:
        temp = ''
        if i >= '1' and i <= '5':
            temp += (int(i) * '.') + ((5 - int(i)) * '-')
        else:
            temp += int(fabs(int(i) - 5)) * '-' 
            temp += int(fabs(len(temp) - 5)) * '.'
        morse_code += temp + ' '

    return morse_code


print(morse_number('295'))