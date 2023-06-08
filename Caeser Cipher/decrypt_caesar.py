import string

plain_text = "Hr Gdhb! fnulxvn cx vh bcanjv"# Enter the text you want to decrypt here
shift = 26 - 9 # 26 - the shift number
shift %= 26

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = plain_text.translate(table)

print(encrypted)
