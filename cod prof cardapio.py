import os 
os.system("cls") 

preco_total=0

while True:
    print(""" 
        Prato      valor
            
1 - Picanha         R$ 25,00
2 - Lasanha         R$ 25,00
3 - Strogonoff      R$ 25,00
4 - Bife acebolado  R$ 25,00
5 - Pão com ovo     R$ 25,00

          """) 
    
    opcao=int(input("digite qual prato desejado:")) 


    match opcao:
        case 1:
            prato="picanha"
            preco=25
        case 2:
            prato="lasanha"
            preco=25
        case 3:
            prato="Strogonoff"
            preco=25

        case 4:
            prato="Bife acebolado"
            preco=25
        case 5:
            prato="Pao com ovo"
            preco=5
        case _: 
            print("opçao invalida")
            print("tente novamente")
            preco=0

    preco_total= preco_total + preco

    mais_pedidos=input("Deseja fazer um novo pedido sim ou Nao").lower()

    if mais_pedidos== "Nao":
        break 
    
    os.system("cls")

#print do resultado 

print("n\=== Restaurante ===")
print(f"Total a pagar é {preco_total}")