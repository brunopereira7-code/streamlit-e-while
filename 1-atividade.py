import os 
os.system("cls") 

quantidades_notas=2
soma=0

for i in range(quantidades_notas):
    while True:
        nota=float(input("digite uma nota:")) 

        if nota <0 or nota >10:
            print("a nota valida") 

        else:
            soma +=nota 
            break 

media= soma/quantidades_notas
print(f"sua media é {media:.2f}")