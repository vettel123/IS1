def substitute(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        if letter in key:
            ciphertext += key[letter]
        else:
            ciphertext += letter
    return ciphertext

key = {'a': 'Z', 'b': 'Y', 'c': 'X', 'd': 'W', 'e': 'V', 'f': 'U', 'g': 'T', 'h': 'S', 'i': 'R', 'j': 'Q', 'k': 'P', 'l': 'O', 'm': 'N', 'n': 'M', 'o': 'L', 'p': 'K', 'q': 'J', 'r': 'I', 's': 'H', 't': 'G', 'u': 'F', 'v': 'E', 'w': 'D', 'x': 'C', 'y': 'B', 'z': 'A'}

plaintext = "hello world"
ciphertext = substitute(plaintext, key)
print(ciphertext)  # Output: "svool dliow"
