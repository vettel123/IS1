s = input("Enter plaintext: ")
k = int(input("Enter key: "))

ans = ""

for i in s:
    if i == " ":
        ans += 0
    else:
        ans += chr((ord(i) + k - 97 )%26 + 97)

    print("Encrypted text is: ",ans)


b = input("Enter ciphertext: ")
k = int(input("Enter key: "))
dec_ans = ""

for i in b:
    if i == " ":
        dec_ans += 0
    else:
        dec_ans += chr((ord(i) - k - 97 + 26)%26 + 97)

    print("Decrypted text is: ",dec_ans)


