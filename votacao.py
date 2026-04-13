# Importa as bibliotecas necessárias
import streamlit as st
from supabase import create_client

# =========================
# CONEXÃO COM O SUPABASE
# =========================

# Pega as credenciais armazenadas no Streamlit Secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

# Cria a conexão com o banco Supabase
supabase = create_client(url, key)


# =========================
# CONFIGURAÇÃO DA PÁGINA
# =========================

st.set_page_config(page_title="Votação de Desafios", layout="centered")


# =========================
# CONTROLE DE NAVEGAÇÃO
# =========================

# Define a página inicial se ainda não existir
if 'pagina' not in st.session_state:
    st.session_state.pagina = 'lista'

# Função para ir para a página de votação
def ir_para_votacao():
    st.session_state.pagina = 'votacao'

# Função para voltar para a lista
def ir_para_lista():
    st.session_state.pagina = 'lista'


# =========================
# HEADER (PARTE SUPERIOR)
# =========================

col_logo, col_user = st.columns([4, 1])
with col_user:
    st.markdown("Usuário: Alunos")

st.divider()


# =========================
# PÁGINA 1 - LISTA DE DESAFIOS
# =========================

if st.session_state.pagina == 'lista':

    with st.container(border=True):
        st.write("### Desafio 01 - A Realidade vs. A Teoria")
        st.caption("em andamento")

        # Botão para acessar o desafio
        if st.button("Acessar Desafio", use_container_width=True):
            ir_para_votacao()
            st.rerun()


# =========================
# PÁGINA 2 - VOTAÇÃO
# =========================

elif st.session_state.pagina == 'votacao':

    # Botão para voltar
    if st.button("Voltar para lista"):
        ir_para_lista()
        st.rerun()

    st.divider()
    st.markdown("#### Desafio 01 | Votação")

    # Detalhes do desafio
    with st.expander("Ver detalhes do desafio", expanded=True):
        st.write("Por que isso acontece?")
        st.write("Justifique sua resposta com base nos testes realizados.")

    st.divider()

    # Área de votação
    st.write("### Escolha sua nota para a apresentação:")

    # Criação dos checkboxes
    col1, col2, col3 = st.columns(3)

    with col1:
        bom = st.checkbox("Bom")
    with col2:
        regular = st.checkbox("Regular")
    with col3:
        ruim = st.checkbox("Ruim")

    # Identificação do usuário (simples)
    usuario = "Aluno1"

    # Botão de envio do voto
    if st.button("Enviar Voto", type="primary"):

        # Validação: mais de uma opção marcada
        if sum([bom, regular, ruim]) > 1:
            st.error("Selecione apenas uma opção.")

        # Validação: nenhuma opção marcada
        elif sum([bom, regular, ruim]) == 0:
            st.warning("Selecione uma nota antes de enviar.")

        else:
            # Define o voto escolhido
            voto = "Bom" if bom else "Regular" if regular else "Ruim"

            try:
                # Verifica se o usuário já votou nesse desafio
                existente = supabase.table("votos") \
                    .select("*") \
                    .eq("usuario", usuario) \
                    .eq("desafio", "Desafio 01") \
                    .execute()

                # Se já votou, bloqueia
                if existente.data:
                    st.error("Você já votou neste desafio.")

                else:
                    # Insere o voto no banco de dados
                    supabase.table("votos").insert({
                        "usuario": usuario,
                        "desafio": "Desafio 01",
                        "voto": voto
                    }).execute()

                    st.success(f"Voto '{voto}' enviado com sucesso.")

            # Tratamento de erro de conexão
            except Exception as e:
                st.error(f"Erro ao conectar com o banco: {e}")


    # =========================
    # EXIBIÇÃO DOS RESULTADOS
    # =========================

    st.divider()
    st.write("### Resultados")

    try:
        # Busca todos os votos do desafio
        dados = supabase.table("votos") \
            .select("*") \
            .eq("desafio", "Desafio 01") \
            .execute()

        # Se houver dados, mostra na tela
        if dados.data:
            st.write(dados.data)
        else:
            st.info("Nenhum voto registrado ainda.")

    except Exception as e:
        st.error(f"Erro ao buscar dados: {e}")
