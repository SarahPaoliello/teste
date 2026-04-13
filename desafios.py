# =========================
# IMPORTAÇÕES
# =========================

import streamlit as st
from supabase import create_client
import pandas as pd


# =========================
# CONEXÃO COM SUPABASE
# =========================

# Pega as credenciais do arquivo secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

# Cria a conexão com o banco
supabase = create_client(url, key)


# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(page_title="Cadastro de Desafios", layout="centered")

st.title("Cadastro de Desafios")


# =========================
# FUNÇÕES CRUD
# =========================

# CREATE - Criar novo desafio
def criar_desafio(titulo, descricao):
    return supabase.table("desafios").insert({
        "titulo": titulo,
        "descricao": descricao
    }).execute()


# READ - Listar desafios
def listar_desafios():
    return supabase.table("desafios").select("*").execute()


# UPDATE - Atualizar desafio
def atualizar_desafio(id, titulo, descricao):
    return supabase.table("desafios") \
        .update({
            "titulo": titulo,
            "descricao": descricao
        }) \
        .eq("id", id) \
        .execute()


# DELETE - Deletar desafio
def deletar_desafio(id):
    return supabase.table("desafios") \
        .delete() \
        .eq("id", id) \
        .execute()


# =========================
# INTERFACE - CRIAR DESAFIO
# =========================

st.subheader("Novo Desafio")

# Campos de entrada
titulo = st.text_input("Título do desafio")
descricao = st.text_area("Descrição do desafio")

# Botão de criação
if st.button("Criar Desafio"):
    if titulo and descricao:
        criar_desafio(titulo, descricao)
        st.success("Desafio criado com sucesso")
    else:
        st.warning("Preencha todos os campos")


# =========================
# INTERFACE - LISTAR DESAFIOS
# =========================

st.divider()
st.subheader("Desafios Cadastrados")

dados = listar_desafios()

# Verifica se há dados
if dados.data:
    df = pd.DataFrame(dados.data)

    # Mostra tabela
    st.write(df)

    st.divider()

    # =========================
    # ATUALIZAR DESAFIO
    # =========================

    st.subheader("Atualizar Desafio")

    id_update = st.number_input("ID do desafio para atualizar", step=1)
    novo_titulo = st.text_input("Novo título")
    nova_descricao = st.text_area("Nova descrição")

    if st.button("Atualizar"):
        if id_update and novo_titulo and nova_descricao:
            atualizar_desafio(id_update, novo_titulo, nova_descricao)
            st.success("Desafio atualizado com sucesso")
        else:
            st.warning("Preencha todos os campos para atualizar")


    # =========================
    # DELETAR DESAFIO
    # =========================

    st.subheader("Deletar Desafio")

    id_delete = st.number_input("ID do desafio para deletar", step=1)

    if st.button("Deletar"):
        if id_delete:
            deletar_desafio(id_delete)
            st.success("Desafio deletado com sucesso")
        else:
            st.warning("Informe um ID válido")

else:
    st.info("Nenhum desafio cadastrado ainda.")
