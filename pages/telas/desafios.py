import streamlit as st

from services.desafio_service import (
    listar_desafios,
    deletar_desafio
)

from services.participacao_service import (
    participar_desafio,
    listar_participantes,
    concluir_desafio,
    cancelar_participacao
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

        participantes = listar_participantes(
            desafio["id"]
        )

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

            st.divider()

            if participantes:

                st.write("Participantes:")

                for p in participantes:

                    st.write(
                        f"- {p['usuarios']['nome']}"
                    )

            else:

                st.info(
                    "Nenhum participante ainda"
                )

            participando = any(

                p["usuario_id"] == usuario["id"]

                for p in participantes
            )

            st.divider()

            # PARTICIPAR

            if not participando:

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

                    else:

                        st.warning(
                            "Você já participa"
                        )

                    st.rerun()

            # CANCELAR PARTICIPAÇÃO

            else:

                st.success(
                    "Você participa deste desafio"
                )

                if desafio["status"] != "concluido":

                    col1, col2 = st.columns(2)

                    with col1:

                        if st.button(
                            "Concluir desafio",
                            key=f"concluir_{desafio['id']}"
                        ):

                            concluir_desafio(
                                desafio["id"],
                                usuario["id"]
                            )

                            st.success(
                                "Desafio concluído"
                            )

                            st.rerun()

                    with col2:

                        if st.button(
                            "Cancelar participação",
                            key=f"cancelar_{desafio['id']}"
                        ):

                            cancelar_participacao(
                                desafio["id"],
                                usuario["id"]
                            )

                            st.warning(
                                "Participação cancelada"
                            )

                            st.rerun()

            st.divider()

            # PERMISSÃO DE EDIÇÃO

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

            # BLOQUEAR EDIÇÃO SE CONCLUÍDO

            if (
                pode_editar
                and desafio["status"] != "concluido"
            ):

                col1, col2 = st.columns(2)

                with col1:

                    if st.button(
                        "Editar",
                        key=f"editar_{desafio['id']}"
                    ):

                        st.session_state.desafio_editar = (
                            desafio["id"]
                        )

                        st.session_state.pagina = (
                            "editar_desafio"
                        )

                        st.rerun()

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
