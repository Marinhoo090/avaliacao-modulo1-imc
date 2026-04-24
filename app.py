import streamlit as st

st.title("Calculadora iMC ")
st.subheader("Meu primeiro programa Streamlit ")

altura = st.number_input("Digite a sua altura: ", min_value = 0.0)
peso = st.number_input("Digite o seu peso: ", min_value = 0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    st.success(f"Seu imc é: {imc:.2f}")

    if imc < 18.5:
        st.image("https://tse1.mm.bing.net/th/id/OIP.rjGfEHhlYsfXqGGKCUB0RwHaJ4?rs=1&pid=ImgDetMain&o=7&rm=3",width = 150)
        st.error("Abaixo do peso.")
    elif imc < 24.9:
        st.image("https://st2.depositphotos.com/1552219/8658/i/450/depositphotos_86585046-stock-photo-success-check-win.jpg" ,width=150)
        st.success("Peso normal.")
    elif imc < 29.9:
        st.image("https://i.pinimg.com/originals/de/dd/15/dedd157bf4f12c42966ed0f4e78dd1af.png " ,width=150)
        st.warning("Sobrepeso")
    elif imc < 34.9:
        st.image("https://dublagembrasileira.com.br/wp-content/uploads/2022/06/nhonho_chaves.jpg ", width=150)
        st.error("Obesidade Grau I")
    elif imc < 39.9:
        st.image("https://static.wikia.nocookie.net/b82d3c0f-f68a-4e0b-8b24-ce5f47c2eae1/scale-to-width/755" ,width=150)
        st.error("Obesidade grau II")
    else:
        if imc > 40.0:
            st.image("https://i.ytimg.com/vi/ojvDvsJv3eQ/maxresdefault.jpg" ,width=160)
            st.error("Obesidade Grau III (mórbida)")
    