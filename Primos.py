def is_prime():
    c = 0
    for i in range(1,n+1):
        if (n%i)==0:
            c=c + 1
    if c==2:
        print ("Is a prime number.")
    else:
        print ("Is NOT a prime number.")

n=int(input("Ingrese un numero: "))
is_prime()