import os 
os.system("cls") 

soma=0
quantidade_notas=0

while True:
    nota= float(input("digite uma nota:")) 
    #quantidades_notas=quantidades_notas +1
    #soma=soma + nota
    quantidade_notas +=1
    soma += nota 
    resposta = input("Deseja inserir mais uma nota? \n use s ou n:").lower() 

    if resposta == "n":
        break

media=soma/quantidade_notas 
print(f"media é {media}")