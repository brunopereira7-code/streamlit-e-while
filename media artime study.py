import os 
os.system("cls") 

soma=0
quantidade_notas=0

while True:
    nota=int(input("Digite a sua nota")) 
    if nota <2:
        break
    quantidade_notas=+1 
    soma=+nota
    
media=soma/quantidade_notas

print(f"sua media é {media}")