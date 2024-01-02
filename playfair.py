def generate_playfair_key(key):
    key = key.replace("J", "I")  # Gantikan 'J' dengan 'I' (aturan Playfair)
    key = "".join(sorted(set(key), key=key.index))  # Hilangkan duplikat dan urutkan

    # Buat matriks 5x5
    matrix = [['' for _ in range(5)] for _ in range(5)]
    chars = [char for char in key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ']

    for i in range(5):
        for j in range(5):
            matrix[i][j] = chars[i * 5 + j]

    return matrix


def find_char(char, key_matrix):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j


def playfair_encrypt(plaintext, key):
    plaintext = plaintext.replace("J", "I")  # Gantikan 'J' dengan 'I' (aturan Playfair)
    plaintext = "".join(filter(str.isalpha, plaintext.upper()))  # Hanya ambil karakter alfabet dan ubah ke uppercase

    key_matrix = generate_playfair_key(key)

    encrypted_text = ""
    i = 0

    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_char(char1, key_matrix)
        row2, col2 = find_char(char2, key_matrix)

        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 5]
            encrypted_text += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 5][col1]
            encrypted_text += key_matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_text += key_matrix[row1][col2]
            encrypted_text += key_matrix[row2][col1]

        i += 2

    return encrypted_text


def playfair_decrypt(ciphertext, key):
    key_matrix = generate_playfair_key(key)

    decrypted_text = ""
    i = 0

    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]

        row1, col1 = find_char(char1, key_matrix)
        row2, col2 = find_char(char2, key_matrix)

        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 5]
            decrypted_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 5][col1]
            decrypted_text += key_matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]

        i += 2

    return decrypted_text


# Contoh penggunaan
key = "KEYWORD"
plaintext = "HELLO WORLD"
ciphertext = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
