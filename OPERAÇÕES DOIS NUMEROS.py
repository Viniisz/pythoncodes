

#### OPERAÇÕES COM DOIS NÚMEROS - SEXTA-FEIRA 3 DE FEVEREIRO DE 2023 - 16:45 ####

# import tkinter as tk

print("\n\tWelcome to the Python Calculator\n")   

number_one = float(input("Digite o primeiro número: "))   
number_two = float(input("Digite o segundo número: "))    

print("\nPara somar: Soma\n" "Para subtrair: Sub\n" "Para divisão: Div\n" "Para multiplicação: Mult\n" )


operation = input("\nQual operação deseja realizar: " )    


def math ():

    if((operation == "Soma") or (operation == "soma")):   
       summ = (number_one + number_two)                   
       print("\nA soma é: ", "%.2f" % summ, "\n")


    elif ((operation == "Sub") or (operation == "sub")):
         sub = (number_one - number_two)                    
         print("\nA Subtração é: ", "%.2f" % sub, "\n")


    if  ((operation == "Div") or (operation == "div")):
        div = (number_one / number_two)                    
        print("\nA Divisão é: ", "%.2f" % div,"\n")


    elif ((operation == "Mult") or (operation == "mult")):
         mult = (number_one * number_two)                  
         print("\nA Multiplicação é: ", "%.2f" % mult, "\n")

math()