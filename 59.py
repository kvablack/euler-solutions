def decrypt(seq, key):
    fullkey = key * int(len(seq) / len(key) + 1)
    return [x ^ y for x, y in zip(seq, fullkey)]

with open("p059_cipher.txt", "r") as f:
    ciphertext = list(map(int, f.readlines()[0].split(",")))
    keys = ((x, y, z) for x in range(97, 123) for y in range(97, 123) for z in range(97, 123))
    for key in keys:
        plaintext = decrypt(ciphertext, key)
        if all(32 <= x <= 122 for x in plaintext):
            print("".join(list(map(chr, plaintext))))
            print(sum(plaintext))
