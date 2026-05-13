from database.conexao import supabase


def registrar_voto(usuario_id, apresentacao_id, nota):

    verificar = (
        supabase
        .table("votos")
        .select("id")
        .eq("usuario_id", usuario_id)
        .eq("apresentacao_id", apresentacao_id)
        .execute()
    )

    if verificar.data:
        return "Você já votou"

    return (
        supabase
        .table("votos")
        .insert({
            "usuario_id": usuario_id,
            "apresentacao_id": apresentacao_id,
            "nota": nota
        })
        .execute()
    )


def listar_votos():

    return (
        supabase
        .table("votos")
        .select("*")
        .execute()
    )
