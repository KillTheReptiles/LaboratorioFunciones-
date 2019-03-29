
def a_power_b(a,b):
    p=1
    for i in range (1,b+1):
        p=p*a
    print("Es: ", p)
while True:
    a=int(input("Ingrese un numero: "))
    b=int(input("Ingrese un exponente: "))
    if a==0:
        print("Fin")
        break
    a_power_b(a,b)












