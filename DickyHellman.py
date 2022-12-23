p = int(input("Enter p: "))
g = int(input("Enter g: "))

a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

Xa = (g**a)%p
Xb = (g**b)%p

Ka = (Xb**a)%p
Kb = (Xa**b)%p

if(Ka == Kb):
    print("Start communication!")
else:
    print("Error")