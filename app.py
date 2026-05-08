import streamlit as st

st.title("Calculadora iMC ")
st.subheader("Meu primeiro programa Streamlit ")

altura = st.number_input("Digite a sua altura: ", min_value = 0.0)
peso = st.number_input("Digite o seu peso: ", min_value = 0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    st.success(f"Seu imc é: {imc:.2f}")

    if imc < 18.5:
        st.error("Abaixo do peso.")
    elif imc < 24.9:
        st.success("Peso normal.")
    elif imc < 29.9:
        st.warning("Sobrepeso")
    elif imc < 34.9:
        st.error("Obesidade Grau I")
    elif imc < 39.9:
        st.error("Obesidade grau II")
    else:
        if imc > 40.0:
            st.error("Obesidade Grau III (mórbida)")
    
