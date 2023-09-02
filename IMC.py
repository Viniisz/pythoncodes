
##### CÁLCULO IMC #####

# SEXTA-FEIRA 3 DE FEVEREIRO DE 2023 - 12:33#


height = float(input("\n Type your height: "))  # Entrada de dados da Altura do usuário
weight = float(input(" Type your weight: "))    # Entrada de dados do Peso do usuário  

imc = weight / (height * height)              # Cálculo IMC

print("\n Your IMC is:","%.2f" % imc)  #"%2.f" % = Aproximar os valores 

if (imc < 18.5):
    print("\n Low weight \n")

elif ((imc >= 18.5) and (imc <= 24.99)):
    print("\n Normal weight \n")   

if ((imc >= 25) and (imc <= 29.99)):
    print("\n overweight \n")

elif (imc > 30):
    print("\n obesity \n")   


## FALTA REFINAR MAIS ALGUNS PARAMÊTROS, COMO: ARREDONDAMENTO DO IMC, REALIZAR TESTE ##
## DESENVOLVER INTERFACE ##