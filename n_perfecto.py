def perfect_number(n):
  s=0
  for i in range(1,n):
    if (n%i==0):
      s+=i

  if n==s:
    return True
  else:
    return False

n=int(input("ingrese un numero: "))

if perfect_number(n):
  print("Es un numero perfecto")
else:
  print("No es un numero perfecto")