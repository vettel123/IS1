from math import gcd

p = len("Hello worls")
q = len("this is rsa algo")

def isPrime(num):
    for x in range(2,int(num/2)):
        if(num%x == 0):
            return(False)
        return(True)

def nextPrime(num):
    if(isPrime(num) == True):
        return(num)
    n = int(num/6)
    if(isPrime(6*n + 1) == (True)):
        return(6*n + 1)

p = nextPrime(p)
q = nextPrime(q)

n = p*q
phi = (p-1)*(q-1)
i=2
while True:
    if gcd(i,phi)==1 and i!=p and i!=q:
        e=i
        break
    i+=1
i=1
while True:
    if (i*e)%phi==1 and i!=e:
        d=i
        break
    i+=1
print(f"Value of e is {e}")
print(f"Value of d is {d}")

plaintext = "How are you"

def encryption(pt,e,n):
    a = (len(pt)**e)%n
    print("Enc text is: ",a)
    return a

def decryption(ct,d,n):
    b = (ct**d)%n
    print("Dec text is: ",b)
    return b

ciphertext = encryption(plaintext,e,n)
plt = decryption(ciphertext,d,n) 