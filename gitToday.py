from tabulate import tabulate

name = input('Masukkan Nama Lengkap: ')
hobby = input('Masukkan hobi anda: ')
email = input('Masukkan email anda: ')
nilai_uts = int(input('Masukkan nilai UTS anda: '))
nilai_uas = int(input('Masukkan nilai UAS anda: '))


if (nilai_uts + nilai_uas) <= 125 or nilai_uts <= 60 or nilai_uas <= 60:
    status = 'Gagal'
else:
    status = 'Lulus'


data = [
    ["Nama Lengkap", name],
    ["Hobi", hobby],
    ["E-mail", email],
    ["Nilai UTS", nilai_uts],
    ["Nilai UAS", nilai_uas],
    ["Status", status]
]


print('\n\n--------------------------')
print('|   BERIKUT DATA ANDA    |')
print('--------------------------')
print(tabulate(data, tablefmt="grid"))



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

print("Aku males bgt buset")