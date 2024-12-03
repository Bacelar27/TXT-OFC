# Instale o Streamlit com: pip install streamlit

import streamlit as st

def gerar_arquivo(cnpj_prestador, razao_prestador, cnpj_tomador, razao_tomador, descricao, valor, data_emissao):
    # Layout padrão do arquivo TXT (exemplo simplificado)
    conteudo = f"""
    Prestador: {cnpj_prestador} - {razao_prestador}
    Tomador: {cnpj_tomador} - {razao_tomador}
    Descrição do Serviço: {descricao}
    Valor do Serviço: {valor}
    Data de Emissão: {data_emissao}
    """
    with open("nota_fiscal_lote.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    return "nota_fiscal_lote.txt"

# Título do aplicativo
st.title("Gerador de Notas Fiscais em Lote - Prefeitura de São Paulo")

# Formulário de entrada de dados
st.header("Preencha os dados para gerar o arquivo TXT")
cnpj_prestador = st.text_input("CNPJ do Prestador")
razao_prestador = st.text_input("Razão Social do Prestador")
cnpj_tomador = st.text_input("CNPJ do Tomador")
razao_tomador = st.text_input("Razão Social do Tomador")
descricao = st.text_area("Descrição do Serviço")
valor = st.text_input("Valor do Serviço")
data_emissao = st.date_input("Data de Emissão")

# Botão para gerar o arquivo
if st.button("Gerar Arquivo TXT"):
    if not (cnpj_prestador and razao_prestador and cnpj_tomador and razao_tomador and descricao and valor):
        st.error("Por favor, preencha todos os campos obrigatórios.")
    else:
        arquivo_gerado = gerar_arquivo(cnpj_prestador, razao_prestador, cnpj_tomador, razao_tomador, descricao, valor, data_emissao)
        st.success("Arquivo gerado com sucesso!")
        st.download_button(
            label="Baixar Arquivo TXT",
            data=open(arquivo_gerado, "rb"),
            file_name="nota_fiscal_lote.txt",
            mime="text/plain"
        )
print('Hello world!')