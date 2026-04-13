import streamlit as st
from supabase import create_client
import pandas as pd

# =========================
# CONEXÃO COM SUPABASE
# =========================

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

supabase = create_client(url, key)

st.set_page_config(page_title="Votação de Desafios", layout="centered")

# =========================
# CONTROLE DE PÁGINAS
# =========================

if 'pagina' not in st.session_state:
    st.session_state.pagina = 'lista'

if 'voto_id' not in st.session_state:
    st.session_state.voto_id = None

def ir(pagina):
    st.session_state.pagina = pagina
    st.rerun()

# =========================
# FUNÇÕES CRUD
# =========================

def inserir_voto(usuario, desafio, voto):
    return supabase.table("votos").insert({
        "usuario": usuario,
        "desafio": desafio,
        "voto": voto
    }).execute()

def listar_votos():
    return supabase.table("votos").select("*").execute()

def buscar_voto_por_id(id):
    return supabase.table("votos").select("*").eq("id", id).execute()

def atualizar_voto(id, novo_voto):
    return supabase.table("votos").update({
        "voto": novo_voto
    }).eq("id", id).execute()

def deletar_voto(id):
    return supabase.table("votos").delete().eq("id", id).execute()

# =========================
# HEADER
# =========================

col1, col2 = st.columns([4, 1])
with col2:
    st.markdown("👤 *Aluno*")

st.divider()

# =========================
# PÁGINA LISTA DE DESAFIOS
# =========================

if st.session_state.pagina == 'lista':

    with st.container(border=True):
        st.write("### Desafio 01 - A Realidade vs. A Teoria")
        st.caption("em andamento")

        if st.button("Acessar Desafio"):
            ir('votacao')

    st.divider()

    if st.button("Ver votos cadastrados"):
        ir('visualizar')

# =========================
# PÁGINA VOTAÇÃO (CREATE)
# =========================

elif st.session_state.pagina == 'votacao':

    if st.button("← Voltar"):
        ir('lista')

    st.write("### Votação")

    voto = st.radio("Escolha sua nota:", ["Bom", "Regular", "Ruim"])

    if st.button("Enviar Voto"):
        try:
            inserir_voto("AlunoTeste", "Desafio 01", voto)
            st.success("Voto salvo com sucesso")
        except Exception as e:
            st.error(e)

# =========================
# PÁGINA VISUALIZAR (READ)
# =========================

elif st.session_state.pagina == 'visualizar':

    if st.button("← Voltar"):
        ir('lista')

    st.write("### Votos cadastrados")

    dados = listar_votos()

    if dados.data:
        df = pd.DataFrame(dados.data)
        st.write(df)

        st.divider()
        st.write("Selecione um voto pelo ID")

        id_voto = st.number_input("ID", step=1)

        if st.button("Editar / Excluir"):
            st.session_state.voto_id = id_voto
            ir('editar')

    else:
        st.info("Nenhum voto encontrado")

# =========================
# PÁGINA EDITAR (UPDATE / DELETE)
# =========================

elif st.session_state.pagina == 'editar':

    if st.button("← Voltar"):
        ir('visualizar')

    id_voto = st.session_state.voto_id

    st.write(f"### Editar voto ID {id_voto}")

    dados = buscar_voto_por_id(id_voto)

    if dados.data:

        voto_atual = dados.data[0]["voto"]

        novo_voto = st.radio(
            "Novo voto:",
            ["Bom", "Regular", "Ruim"],
            index=["Bom", "Regular", "Ruim"].index(voto_atual)
        )

        col1, col2 = st.columns(2)

        with col1:
            if st.button("Atualizar"):
                atualizar_voto(id_voto, novo_voto)
                st.success("Voto atualizado")

        with col2:
            if st.button("Excluir"):
                deletar_voto(id_voto)
                st.success("Voto excluído")

    else:
        st.error("Voto não encontrado")
