from database.conexao import supabase
from datetime import datetime


def listar_desafios():

    return (
        supabase
        .table("desafios")
        .select("*")
        .order("id")
        .execute()
    )


def criar_desafio(titulo, descricao, vagas, data_fechamento, usuario_id):

    return (
        supabase
        .table("desafios")
        .insert({
            "titulo": titulo,
            "descricao": descricao,
            "max_participantes": vagas,
            "data_fechamento": data_fechamento,
            "criador_id": usuario_id,
            "status": "aberto"
        })
        .execute()
    )


def editar_desafio(id_desafio, titulo, descricao):

    return (
        supabase
        .table("desafios")
        .update({
            "titulo": titulo,
            "descricao": descricao,
            "editado_em": str(datetime.now())
        })
        .eq("id", int(id_desafio))
        .execute()
    )


def deletar_desafio(id_desafio):

    return (
        supabase
        .table("desafios")
        .delete()
        .eq("id", int(id_desafio))
        .execute()
    )
