import streamlit as st


def tela_home():

    usuario = st.session_state.usuario_logado

    st.title(
        f"Bem-vindo(a), {usuario['nome']}"
    )

    st.divider()

    st.subheader(
        "Desafios disponíveis"
    )

    st.info(
        "Nenhum desafio cadastrado"
    )

    st.divider()

    st.subheader(
        "Desafios disponíveis para votação"
    )

    st.info(
        "Nenhuma apresentação disponível"
    )

    st.divider()

    st.subheader(
        "Mini-provas"
    )

    st.warning(
        "Sistema em construção"
    )
