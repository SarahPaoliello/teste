import streamlit as st

from services.desafio_service import criar_desafio


def tela_criar_desafio():

    st.title("Criar desafio")

    with st.form("form_desafio"):

        titulo = st.text_input(
            "Título"
        )

        descricao = st.text_area(
            "Descrição"
        )

        max_participantes = st.number_input(
            "Máximo de participantes",
            min_value=1,
            step=1
        )

        data_fechamento = st.date_input(
            "Data de fechamento"
        )

        criar = st.form_submit_button(
            "Criar desafio"
        )

    if criar:

        usuario = st.session_state.usuario_logado

        criar_desafio(
            titulo,
            descricao,
            max_participantes,
            data_fechamento,
            usuario["id"]
        )

        st.success(
            "Desafio criado com sucesso"
        )

        st.session_state.pagina = "desafios"

        st.rerun()

    st.divider()

    if st.button("Voltar"):

        st.session_state.pagina = "desafios"

        st.rerun()
