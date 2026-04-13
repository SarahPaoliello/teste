# =========================
# IMPORTAÇÕES
# =========================

import streamlit as st
from supabase import create_client
import pandas as pd


# =========================
# CONEXÃO COM O BANCO
# =========================

# Credenciais do Supabase via secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)


# =========================
# FUNÇÕES CRUD (CAMADA DE DADOS)
# =========================

# CREATE - Inserir voto
def inserir_voto(usuario, desafio, voto):
    return supabase.table("votos").insert({
        "usuario": usuario,
        "desafio": desafio,
        "voto": voto
    }).execute()


# READ - Buscar votos por desafio
def buscar_votos(desafio):
    return supabase.table("votos") \
        .select("*") \
        .eq("desafio", desafio) \
        .execute()


# READ - Verificar se usuário já votou
def verificar_voto(usuario, desafio):
    return supabase.table("votos") \
        .select("*") \
        .eq("usuario", usuario) \
        .eq("desafio", desafio) \
        .execute()


# UPDATE - Atualizar voto (preparado para integração futura)
def atualizar_voto(usuario, desafio, novo_voto):
    return supabase.table("votos") \
        .update({"voto": novo_voto}) \
        .eq("usuario", usuario) \
        .eq("desafio", desafio) \
        .execute()


# DELETE - Remover voto (admin ou testes)
def deletar_voto(usuario, desafio):
    return supabase.table("votos") \
        .delete() \
        .eq("usuario", usuario) \
        .eq("desafio", desafio) \
        .execute()


# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(page_title="Sistema de Votação", layout="centered")


# =========================
# DADOS SIMULADOS (INTEGRAÇÃO FUTURA)
# =========================

# Aqui futuramente virá do sistema de login
if "usuario" not in st.session_state:
    st.session_state.usuario = "AlunoTeste"

# Aqui futuramente virá do sistema de desafios
if "desafio" not in st.session_state:
    st.session_state.desafio = "Desafio 01"


# =========================
# NAVEGAÇÃO
# =========================

if "pagina" not in st.session_state:
    st.session_state.pagina = "lista"

def ir_para_votacao():
    st.session_state.pagina = "votacao"

def ir_para_lista():
    st.session_state.pagina = "lista"


# =========================
# HEADER
# =========================

col1, col2 = st.columns([4, 1])
with col2:
    st.write(f"Usuário: {st.session_state.usuario}")

st.divider()


# =========================
# PÁGINA DE LISTA DE DESAFIOS
# =========================

if st.session_state.pagina == "lista":

    # Simulação de desafios (depois vem do outro grupo)
    desafios = ["Desafio 01"]

    for d in desafios:
        with st.container(border=True):
            st.write(f"### {d}")
            st.caption("em andamento")

            if st.button(f"Acessar {d}"):
                st.session_state.desafio = d
                ir_para_votacao()
                st.rerun()


# =========================
# PÁGINA DE VOTAÇÃO
# =========================

elif st.session_state.pagina == "votacao":

    if st.button("Voltar"):
        ir_para_lista()
        st.rerun()

    st.divider()

    desafio = st.session_state.desafio
    usuario = st.session_state.usuario

    st.write(f"### {desafio} | Votação")

    # Área de voto (melhorado com radio)
    voto = st.radio(
        "Escolha sua nota:",
        ["Bom", "Regular", "Ruim"]
    )

    # Botão de envio
    if st.button("Enviar Voto"):

        try:
            existente = verificar_voto(usuario, desafio)

            if existente.data:
                st.warning("Você já votou. Atualizando voto...")

                atualizar_voto(usuario, desafio, voto)
                st.success("Voto atualizado com sucesso.")

            else:
                inserir_voto(usuario, desafio, voto)
                st.success("Voto registrado com sucesso.")

        except Exception as e:
            st.error(f"Erro: {e}")


    # =========================
    # RESULTADOS
    # =========================

    st.divider()
    st.write("### Resultados")

    try:
        dados = buscar_votos(desafio)

        if dados.data:
            df = pd.DataFrame(dados.data)

            # Mostra tabela
            st.write(df)

            # Gráfico
            contagem = df["voto"].value_counts()
            st.bar_chart(contagem)

        else:
            st.info("Nenhum voto registrado.")

    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
