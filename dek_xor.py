def xor_decrypt(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as fin:
            ciphertext = fin.read()
    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
        return

    key_length = len(key)
    plaintext = bytearray(len(ciphertext))

    for i in range(len(ciphertext)):
        plaintext[i] = ciphertext[i] ^ ord(key[i % key_length])

    with open(output_file, 'wb') as fout:
        fout.write(plaintext)

    print(f"Proses dekripsi selesai. Hasil disimpan di {output_file}")

if __name__ == "__main__":
    input_file = 'cipher.txt'
    output_file = 'plain2.txt'
    key = input("Kata kunci: ")

    if not key:
        print("Kata kunci tidak boleh kosong.")
    else:
        xor_decrypt(input_file, output_file, key)
