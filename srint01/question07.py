def Cipher_Zeroes(N):
    zeros = {'0': 1, '6': 1, '9': 1, '8': 2}
    counter = 0

    for num in N:
        if num in zeros:
            counter += zeros[num]

    if counter == 0:
        return '0'

    if counter % 2 != 0:
        return str(bin(counter + 1))[2:]
    else:
        return str(bin(counter - 1))[2:]