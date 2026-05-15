import streamlit as st


def mostrar_menu():

    with st.sidebar:

        st.title("Challenge System")

        usuario = st.session_state.usuario_logado

        st.write(
            f"Usuário: {usuario['nome']}"
        )

        st.divider()

        if st.button("Home"):
            st.session_state.pagina = "home"
            st.rerun()

        if st.button("Desafios"):
            st.session_state.pagina = "desafios"
            st.rerun()

        if st.button("Votação"):
            st.session_state.pagina = "votacao"
            st.rerun()

        if st.button("Mini-provas"):
            st.session_state.pagina = "mini_provas"
            st.rerun()

        if usuario["tipo_usuario"] == "admin":

            if st.button("Admin"):
                st.session_state.pagina = "admin"
                st.rerun()

        st.divider()

        if st.button("Sair"):

            st.session_state.usuario_logado = None
            st.session_state.pagina = "login"

            st.rerun()

        if st.button("Desafios"):

            st.session_state.pagina = "desafios"

            st.rerun()
