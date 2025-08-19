import streamlit as st
import pandas as pd

sheet_url = "https://docs.google.com/spreadsheets/d/1wqAJBWdS3jncP455KcJ0qpbJgzhVplOVG-JM4u8MvJU/edit#gid=0"
aba_nome = "Página1"

# Conexão com Google Sheets via Streamlit Cloud
conn = st.experimental_connection("gsheets", type="gsheets")

# Lê os dados da aba
df = conn.read(spreadsheet=sheet_url, worksheet=aba_nome)

# Exibição
st.title("📊 Dados da Página 1")
st.dataframe(df, use_container_width=True)
