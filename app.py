import streamlit as st

from utils.session import iniciar_session

from components.navbar import mostrar_menu

from pages.telas.login import tela_login
from pages.telas.cadastro import tela_cadastro
from pages.telas.home import tela_home

from pages.telas.desafios import tela_desafios
from pages.telas.criar_desafio import tela_criar_desafio

st.set_page_config(
    page_title="Challenge System",
    layout="centered"
)

iniciar_session()

pagina = st.session_state.pagina

if st.session_state.usuario_logado:

    mostrar_menu()

if pagina == "login":

    tela_login()

elif pagina == "cadastro":

    tela_cadastro()

elif pagina == "home":

    if not st.session_state.usuario_logado:

        st.session_state.pagina = "login"

        st.rerun()

    tela_home()
