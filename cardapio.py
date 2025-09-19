import os 
os.system("cls") 

print("""Picanha = 25,00
        Lasanha=  20,00 
      Strogonoff =18,00 
      Bife acebolado = 15,00 
      Pão com ovo = 5,00
      """) 

cardapio={ "Picanha25.00"
        "Lasanha=20.00"
        "Strogonoff=18.00"
        "Bife_acebolado=15.00"
        "Pao_com_ovo=5.00"
 }
quantidade_prato=input("Quantos prato gostaria:") 

pratos=input("Digite quais prato voce quer:") .strip() .lower()


for i in range(3):
    while True: 
        if quantidade_prato >=2:
            print("Picanha" \
                "lasanha" \
                "strogonoff"
                "bife acebolado"
                "Pao com ovo") 
            pratos=input("digite qual voce quer")
            break
        if quantidade_prato >5 and  quantidade_prato>10:
            print("Picanha" \
                "lasanha" \
                "strogonoff"
                "bife acebolado"
                "Pao com ovo")
            pratos=input("Digite qual prato voce quer") 
            break
        else:
            print("nao temos esse prato,sorry")


soma=quantidade_prato+pratos

print(f"os prato que voce pediu foi {pratos}")
print(f" conta deu {soma}") 






