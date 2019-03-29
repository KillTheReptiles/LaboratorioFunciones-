def is_prime():
    c = 0
    for i in range(1,n+1):
        if (n%i)==0:
            c=c + 1
    if c==2:
        print ("1")
    elif c>2:
        print ("0")
    else:
        print("-1")

intentos=0
while True:
    try:
        n=int(input("Ingrese un numero: "))
        if n<=0:
            print("Fin")
            break
        else:
            intentos=intentos+1
        is_prime()
    except ValueError:
        print("Solo se admiten numeros")

print("Se han intentado calcuar",intentos,"veces numeros primos")