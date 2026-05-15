import streamlit as st

from services.desafio_service import (
    listar_desafios,
    deletar_desafio
)

from services.participacao_service import (
    participar_desafio,
    listar_participantes
)


def tela_desafios():

    st.title("Desafios")

    if st.button(
        "Criar desafio",
        key="btn_criar_desafio"
    ):

        st.session_state.pagina = "criar_desafio"

        st.rerun()

    st.divider()

    desafios = listar_desafios()

    if not desafios:

        st.info(
            "Nenhum desafio cadastrado"
        )

        return

    usuario = st.session_state.usuario_logado

    for desafio in desafios:

        with st.container(border=True):

            st.subheader(
                desafio["titulo"]
            )

            st.write(
                desafio["descricao"]
            )

            st.write(
                f"Máximo participantes: "
                f"{desafio['max_participantes']}"
            )

            st.write(
                f"Fecha em: "
                f"{desafio['data_fechamento']}"
            )

            st.write(
                f"Status: "
                f"{desafio['status']}"
            )

            participantes = listar_participantes(
                desafio["id"]
            )

            if participantes:

                st.write(
                    "Participantes:"
                )

                for p in participantes:

                    st.write(
                        f"- {p['usuarios']['nome']}"
                    )

            if st.button(
                "Participar",
                key=f"participar_{desafio['id']}"
            ):

                sucesso = participar_desafio(
                    desafio["id"],
                    usuario["id"]
                )

                if sucesso:

                    st.success(
                        "Participação registrada"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Você já participa"
                    )

            pode_editar = (

                usuario["id"]
                == desafio["criador_id"]

                or

                usuario["tipo_usuario"]
                in [
                    "professor",
                    "admin"
                ]
            )

            if pode_editar:

                col1, col2 = st.columns(2)

                with col1:

                    st.button(
                        "Editar",
                        key=f"editar_{desafio['id']}"
                    )

                with col2:

                    if st.button(
                        "Excluir",
                        key=f"excluir_{desafio['id']}"
                    ):

                        deletar_desafio(
                            desafio["id"]
                        )

                        st.success(
                            "Desafio removido"
                        )

                        st.rerun()
