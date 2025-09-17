import streamlit as st
import time


st.title("Laço de repetiçao") 
st.write("Escreva um algoritmo que solcicita duas notas para um aluno " \
        "caso seja menor que 0 ou maior que 10 mostre a pergunta novamente " \
        "calcule e mostre a media aritmetica do aluno")

nota1=st.number_input("digite sua primeria nota:",min_value=0,max_value=10)
nota2=st.number_input("digite sua primeria nota:",min_value=0,max_value=10) 

while True:
    break

media=(nota1+nota2)/2 

if st.button("calcular media:"):
    st.info(f"media é {media}") 

