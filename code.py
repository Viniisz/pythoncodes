

name   = input("\nDigite seu nome: ")
idade  = int(input("Digite sua idade: "))

name2  = input("\nDigite seu nome: ")
idade2 = int(input("Digite sua idade: "))


print("\nSeja bem vindo:",name.upper(),"você tem:",idade,"anos de idade")
print("\nSeja bem vindo:",name2.upper(),"você tem:",idade2,"anos de idade\n")


if idade == idade2:
  print("\nVocês tem a mesma idade.",name.upper(),"tem a mesma idade de",name2.upper(),",ambos tem",idade,"anos de idade.\n")

elif idade > idade2:
    print("\n",name.upper(),"é mais velho que,",name2.upper(),",ele tem",idade,"anos de idade. E",name2.upper(),"tem ",idade2,"anos de idade.\n")

else:
      print("\n",name2.upper(),"é mais velho que",name.upper(),",ele tem",idade2,"anos de idade. E",name.upper(),"tem ",idade,"anos de idade.\n")
