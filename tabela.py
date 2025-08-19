import streamlit as st
import pandas as pd

# ------------------------- CONFIGURAÇÃO -------------------------
sheet_url = "https://docs.google.com/spreadsheets/d/1wqAJBWdS3jncP455KcJ0qpbJgzhVplOVG-JM4u8MvJU/edit#gid=0"
aba_nome = "Página1"

# ------------------------- CONEXÃO GOOGLE SHEETS -------------------------
conn = st.experimental_connection("gsheets", type="gsheets")

# ------------------------- LEITURA DADOS -------------------------
df = conn.read(spreadsheet=sheet_url, worksheet=aba_nome)

# ------------------------- EXIBIR TABELA -------------------------
st.title("📊 Dados da Página 1")
st.dataframe(df, use_container_width=True)
