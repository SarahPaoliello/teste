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

    dados = {

        "titulo": titulo,

        "descricao": descricao,

        "max_participantes": int(
            max_participantes
        ),

        "data_fechamento": data_fechamento.isoformat(),

        "criado_por": int(
            criado_por
        )
    }

    return (
        supabase
        .table("desafios")
        .insert(dados)
        .execute()
    )


def deletar_desafio(id_desafio):

    return (
        supabase
        .table("desafios")
        .delete()
        .eq("id", id_desafio)
        .execute()
    )
