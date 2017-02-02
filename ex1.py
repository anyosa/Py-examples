# -*- coding: utf-8 -*-

nota1 = int(input("entre uma nota:"))
nota2 = int(input("entre uma nota:"))
nota3 = int(input("entre uma nota:"))
nota4 = int(input("entre uma nota:"))

media=(nota1+nota2+nota3+nota4)/4

if (media>=6):
    resultado = 'aprovado'
    print(resultado)
elif (media>=5):
    resultado = 'rec'
    print(resultado)
else:
    resultado = 'reprovado'
    print(resultado)

print ("sua media e:", media)
