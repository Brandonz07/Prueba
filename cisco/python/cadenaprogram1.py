# Cifrado César.
text = input("Ingresa tu mensaje: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Cifrado César - descifrar un mensaje.
# cipher = input('Ingresa tu criptograma: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)

# print(text)

#Procesador de Números.

# line = input("Ingresa una línea de números, sepáralos con espacios: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("El total es:", total)
# except:
#     print(substr, "no es un numero.")

# Validador IBAN.

# iban = input("Ingresa un IBAN, por favor: ")
# iban = iban.replace(' ','')

# if not iban.isalnum():
#     print("Has introducido caracteres no válidos.")
# elif len(iban) < 15:
#     print("El IBAN ingresado es demasiado corto.")
# elif len(iban) > 31:
#     print("El IBAN ingresado es demasiado largo.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     iban = int(iban2)
#     if iban % 97 == 1:
#         print("El IBAN ingresado es válido.")
#     else:
#         print("El IBAN ingresado no es válido.")
