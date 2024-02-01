def to_binary(decimal):
    binary = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        binary = str(decimal %2) + binary
        decimal = decimal // 2
    return binary

def to_oktal(decimal):
    oktal = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        oktal = str(decimal % 8) + oktal
        decimal = decimal // 8
    return oktal

def to_hexa(decimal):
    hexa = ''
    if decimal == 0:
        return '0'
    while decimal > 0:
        hexa = str(decimal % 16) + hexa
        decimal = decimal // 16
    return hexa


user_input = input('Input: ')

if user_input.isdigit():
    decimal = int(user_input)
else:
    decimal = ord(user_input)

print('Desimal: ', decimal)
print('Binary: ', to_binary(decimal))
print('Oktal: ', to_oktal(decimal))
print('Hexadesimal: ', to_hexa(decimal))