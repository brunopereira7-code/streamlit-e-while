import streamlit as st

st.title("login")

login_cadastrado="josevaldo123"
senha_cadastrada="12345" 

login=st.text_input("digite seu login").lower()
senha=st.text_input("digite sua senha",type="password")

if st.button("iniciar"):
    if login==login_cadastrado and senha==senha_cadastrada:
        st.write("bem-vindo") 
        st.balloons() 
        

    else:
        st.write("Dados incorretos") 

    

