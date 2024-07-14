def xor_encrypt(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as fin:
            plaintext = fin.read()
    except FileNotFoundError:
        print(f"File {input_file} tidak ditemukan.")
        return

    key_length = len(key)
    ciphertext = bytearray(len(plaintext))

    for i in range(len(plaintext)):
        ciphertext[i] = plaintext[i] ^ ord(key[i % key_length])

    with open(output_file, 'wb') as fout:
        fout.write(ciphertext)

    print(f"Proses enkripsi selesai. Hasil disimpan di {output_file}")

if __name__ == "__main__":
    input_file = 'plain.txt'
    output_file = 'cipher.txt'
    key = input("Kata kunci: ")

    if not key:
        print("Kata kunci tidak boleh kosong.")
    else:
        xor_encrypt(input_file, output_file, key)
