import streamlit as st
from supabase import create_client
import pandas as pd

# =========================
# CONEXÃO COM BANCO
# =========================

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.set_page_config(page_title="Desafios", layout="centered")

st.title("Cadastro de Desafios")

# =========================
# FUNÇÕES CRUD
# =========================

# CREATE
def criar_desafio(titulo, descricao):
    return supabase.table("desafios").insert({
        "titulo": titulo,
        "descricao": descricao
    }).execute()

# READ
def listar_desafios():
    return supabase.table("desafios").select("*").execute()

# UPDATE
def atualizar_desafio(id, titulo, descricao):
    return supabase.table("desafios") \
        .update({
            "titulo": titulo,
            "descricao": descricao
        }) \
        .eq("id", id) \
        .execute()

# DELETE
def deletar_desafio(id):
    return supabase.table("desafios") \
        .delete() \
        .eq("id", id) \
        .execute()

# =========================
# INTERFACE
# =========================

st.subheader("Novo Desafio")

titulo = st.text_input("Título do desafio")
descricao = st.text_area("Descrição")

if st.button("Criar Desafio"):
    if titulo and descricao:
        criar_desafio(titulo, descricao)
        st.success("Desafio criado com sucesso")
    else:
        st.warning("Preencha todos os campos")

st.divider()

st.subheader("Lista de Desafios")

dados = listar_desafios()

if dados.data:
    df = pd.DataFrame(dados.data)
    st.write(df)

    # opção simples de deletar
    id_deletar = st.number_input("ID para deletar", step=1)

    if st.button("Deletar Desafio"):
        deletar_desafio(id_deletar)
        st.success("Desafio removido")

else:
    st.info("Nenhum desafio cadastrado")
