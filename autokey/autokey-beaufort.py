# Beaufort Cipher
plain_text = "Hello World!"
key = "polke"
plain_text_length = len(plain_text)
key_length = len(key)

# ulang key agar panjang key = panjang plain text
generated_key = []
key_pointer = 0
autokey_pointer = 0
for i in range(plain_text_length):
    if plain_text[i].isalpha():
        if (key_pointer < key_length):
            generated_key.append(key[key_pointer])
            key_pointer += 1
        else:
            if plain_text[autokey_pointer].isalpha():
                generated_key.append(plain_text[autokey_pointer])
                autokey_pointer += 1
    else:
        generated_key.append(plain_text[i])

# enkripsi
cipher_text = ""
ascii_plain_text = []
ascii_key = []
for index in range(plain_text_length):
    if plain_text[index].isalpha():
        # mengubah ASCII menjadi indeks 0-25
        ascii_plain_text.append(
            ord(plain_text[index]) - 65
            if plain_text[index].isupper()
            else ord(plain_text[index]) - 97
        )
        ascii_key.append(
            ord(generated_key[index]) - 65
            if generated_key[index].isupper()
            else ord(generated_key[index]) - 97
        )
        # mencari ciphertext
        value = (ascii_key[index] - ascii_plain_text[index]) % 26
        cipher_text += chr(value +
                           65) if plain_text[index].isupper() else chr(value + 97)
    else:
        ascii_plain_text.append(ord(plain_text[index]))
        ascii_key.append(ord(generated_key[index]))
        cipher_text += plain_text[index]

# dekripsi
decrypted_text = ""
cipher_text_length = len(cipher_text)
ascii_cipher_text = []
ascii_key = []
for index in range(cipher_text_length):
    if cipher_text[index].isalpha():
        # mengubah ASCII menjadi indeks 0-25
        ascii_cipher_text.append(
            ord(cipher_text[index]) - 65
            if cipher_text[index].isupper()
            else ord(cipher_text[index]) - 97
        )
        ascii_key.append(
            ord(generated_key[index]) - 65
            if generated_key[index].isupper()
            else ord(generated_key[index]) - 97
        )
        # mencari ciphertext
        value = (ascii_key[index] - ascii_cipher_text[index]) % 26
        decrypted_text += chr(value +
                              65) if plain_text[index].isupper() else chr(value + 97)
    else:
        ascii_cipher_text.append(ord(plain_text[index]))
        ascii_key.append(ord(generated_key[index]))
        decrypted_text += plain_text[index]

print("Plain text:", plain_text)
print("Cipher text:", cipher_text)
print("Decrypted text:", decrypted_text)
