def encrypt(plain_text, key):
    cipher_text = ""
    key = int(key)

    for i in range(len(plain_text)):
        current_char = ord(plain_text[i].upper())
        if current_char >= 65 and current_char <= 90:
            cipher_text += chr(
                (current_char + key - 65) % 26 + 65
            )
        else: 
            cipher_text += plain_text[i]
    return cipher_text

def decrypt(cipher_text, key):
    plain_text = ""
    key = int(key)

    for i in range(len(cipher_text)):
        current_char = ord(cipher_text[i].upper())
        if current_char >= 65 and current_char <= 90:
            plain_text += chr(
                (current_char - key - 65) % 26 + 65
            )
        else: 
            plain_text += cipher_text[i]
    return plain_text

if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Cryptography")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("Ketik 0 untuk keluar program")

        choice = int(input("Pilih menu: "))

        if choice == 0: break
        elif choice == 1:
            message = input("Masukkan plain text: ")
            key = int(input("Masukkan kunci: "))
            cipher_text = encrypt(message, key)
            print(f"Cipher text: {cipher_text}")
        elif choice == 2:
            message = input("Masukkan cipher text: ")
            key = int(input("Masukkan kunci: "))
            plain_text = decrypt(message, key)
            print(f"Plain text: {plain_text}")
        else:
            print("Pilihan tidak valid")
        
        cont = input("Lanjut? (y/t) ")
        if cont == "t":
            break