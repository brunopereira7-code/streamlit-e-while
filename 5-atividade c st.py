import streamlit as st

st.title("Cadastrado")


login_cadastrado="perorin" 
senha_cadastrada="123" 

st.session_state.setdefault("desabilitar",False)
st.session_state.setdefault("tentativas",0)

login=st.text_input("Digite seu login:",disabled=st.session_state.desabilitar)
senha=st.text_input("Digite seu login:",type="password",disabled=st.session_state.desabilitar) 

if st.button("iniciar"):
    if login == login_cadastrado and senha == senha_cadastrada:
        st.success("bem vindo") 
        st.balloons()
    else:
        st.session_state.tentativas += 1
        if st.session_state.tentativas <=3:
            st.warning("login ou senha incorreta") 
            

        else: 
            st.session_state.desabilitar=True



