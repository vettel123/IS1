import hashlib

text = "It was easy to remember, because I did that"

inputlines = text.split(" .")
inputlines = list(map(str.encode, inputlines))
print("Input lines: ",inputlines)
print()

hash_obj = list(map(hashlib.sha1, inputlines))
hash_val = list(map(type(hash_obj[0]).hexdigest, hash_obj))

print("hash value: ", hash_val)
print()

def MerkelRoot(hash_val):
    counter = 0
    merkel_root = " "

    for index in range(len(hash_val)):
        if index == 2**counter:
            merkel_root += hash_val[index-1]
            counter += 1

        else:
            merkel_root += hash_val[index]

    return merkel_root

merkel_root = MerkelRoot(hash_val)
print("Merkel root: ",merkel_root)