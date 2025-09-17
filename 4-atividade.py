import os 
os.system("cls") 

tentativas=0
login_salvo ="pero"
senha_salva ="12345" 

for i in range(3):
    while True:
        if tentativas>=3:
            break
        print(f"\n Tentativa:{tentativas+1}") 
        login=input("digite seu login:") 
        senha=input("digite sua senha:") 

        if login == login_salvo and senha == senha_salva:
            print("bem-vindo") 
            break 

        else:
            print("login ou senha invalidas") 
            tentativas +=1 

print("Fim")