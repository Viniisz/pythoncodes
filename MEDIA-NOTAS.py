
##### CÁLCULO MÉDIA DE NOTAS #####

# QUINTA-FEIRA 2 DE FEVEREIRO DE 2023 - 15:30 #

print("\nHello welcome to note system")
print("\nType your name and notes")


name = input("\nType your name: ")

print("\nHello, ", name)

np1 = float(input("\nType your first note: "))
np2 = float(input("Type your second note: "))

media = (np1 + np2) / 2


if (media >= 7) :  
   print("\nYou are approved, YESSIR!!")

else:
   print("\nYou are not approved, DAMN!! " + "Good lucky on the next")

print("\nYour media is: ", media, "\n")

## FALTA REALIZAR MAIS TESTES, FUTURAMENTE DESENVOLVER INTERFACE ##
