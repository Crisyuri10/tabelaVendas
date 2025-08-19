import streamlit as st
import pandas as pd
import pygsheets

# ----------------------- AUTENTICAÇÃO GOOGLE SHEETS -----------------------
credenciais_dict = st.secrets["gcp_service_account"]  # pega o dict direto
gc = pygsheets.authorize(service_account_info=credenciais_dict)

sheet_url = "https://docs.google.com/spreadsheets/d/1wqAJBWdS3jncP455KcJ0qpbJgzhVplOVG-JM4u8MvJU/edit#gid=0"

# ----------------------- LEITURA DADOS -----------------------
aba = gc.open_by_url(sheet_url).worksheet_by_title("Página1")
df = pd.DataFrame(aba.get_all_records())

# ----------------------- EXIBIR TABELA -----------------------
st.title("📊 Dados da Página 1")
st.dataframe(df, use_container_width=True)
