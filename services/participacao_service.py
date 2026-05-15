from database.conexao import supabase


def participar_desafio(
    desafio_id,
    usuario_id
):

    verificar = (
        supabase
        .table("participantes_desafio")
        .select("*")
        .eq("desafio_id", desafio_id)
        .eq("usuario_id", usuario_id)
        .execute()
    )

    if verificar.data:

        return False

    supabase.table(
        "participantes_desafio"
    ).insert({

        "desafio_id": desafio_id,

        "usuario_id": usuario_id

    }).execute()

    return True


def listar_participantes(
    desafio_id
):

    resposta = (
        supabase
        .table("participantes_desafio")
        .select("""
            *,
            usuarios(nome)
        """)
        .eq("desafio_id", desafio_id)
        .execute()
    )

    return resposta.data
def cancelar_participacao(
    desafio_id,
    usuario_id
):

    supabase.table(
        "participantes_desafio"
    ).delete().eq(
        "desafio_id",
        desafio_id
    ).eq(
        "usuario_id",
        usuario_id
    ).execute()
