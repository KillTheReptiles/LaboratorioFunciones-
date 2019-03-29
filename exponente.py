def a_power_b(a,b):
    p=1
    for i in range (1,b+1):
        p=p*a
    print("Es: ", p)


a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un exponente: "))
a_power_b(a,b)
