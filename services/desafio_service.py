from database.conexao import supabase


def listar_desafios():

    resposta = (
        supabase
        .table("desafios")
        .select("*")
        .order("id")
        .execute()
    )

    return resposta.data


def criar_desafio(
    titulo,
    descricao,
    max_participantes,
    data_fechamento,
    criado_por
):

    supabase.table("desafios").insert({

        "titulo": titulo,
        "descricao": descricao,
        "max_participantes": max_participantes,
        "data_fechamento": str(data_fechamento),
        "criado_por": criado_por

    }).execute()


def deletar_desafio(id_desafio):

    supabase.table("desafios")\
        .delete()\
        .eq("id", id_desafio)\
        .execute()
