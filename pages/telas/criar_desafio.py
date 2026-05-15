from database.conexao import supabase
import streamlit as st

from services.desafio_service import criar_desafio

def listar_desafios():

    resposta = (
        supabase
        .table("desafios")
        .select("*")
        .order("id")
        .execute()
    )
def tela_criar_desafio():

    return resposta.data
    st.title("Criar desafio")

    with st.form("form_desafio"):

def criar_desafio(
    titulo,
    descricao,
    max_participantes,
    data_fechamento,
    criado_por
):
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

    dados = {
        data_fechamento = st.date_input(
            "Data de fechamento"
        )

        "titulo": titulo,
        criar = st.form_submit_button(
            "Criar desafio"
        )

        "descricao": descricao,
    if criar:

        "max_participantes": int(
            max_participantes
        ),
        usuario = st.session_state.usuario_logado

        "data_fechamento": data_fechamento.isoformat(),
        criar_desafio(
            titulo,
            descricao,
            max_participantes,
            data_fechamento,
            usuario["id"]
        )

        "criado_por": int(
            criado_por
        st.success(
            "Desafio criado com sucesso"
        )
    }

    return (
        supabase
        .table("desafios")
        .insert(dados)
        .execute()
    )
        st.session_state.pagina = "desafios"

        st.rerun()

    st.divider()

    if st.button("Voltar"):

def deletar_desafio(id_desafio):
        st.session_state.pagina = "desafios"

    return (
        supabase
        .table("desafios")
        .delete()
        .eq("id", id_desafio)
        .execute()
    )
        st.rerun()
