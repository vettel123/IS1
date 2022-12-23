def get_key(s,k):
    if(len(s)==len(k)):
        return k
    diff = len(s)-len(k)
    for i in range(diff):
        k += (k[i%len(k)])
    return k

s = input("Enter plaintext without spaces: ").upper()
k = input("Enter key: ").upper()


def encrypt(s,k):
    k = get_key(s,k)
    ans = ""
    for i in range(len(s)):
        ans += chr(ord('A') + (ord(s[i]) + ord(k[i]) )%26)   
    return ans

print("Enc txt is: ",encrypt(s,k))

b = encrypt(s,k).upper()


def decrypt(b,k):
    k = get_key(b,k)
    dec_ans = ""
    for j in range(len(b)):
        dec_ans += chr(ord('A') + (ord(b[j]) - ord(k[j]) + 26)%26)
    return dec_ans

print("The decrypted text is: ", decrypt(b,k))