import streamlit as st
import pandas as pd
import pygsheets
import os
import json

# ----------------------- AUTENTICAÇÃO GOOGLE SHEETS -----------------------
credenciais_path = "cred.json"

if os.path.exists(credenciais_path):
    # Ambiente local
    gc = pygsheets.authorize(service_file=credenciais_path)
else:
    # Streamlit Cloud -> pega das secrets
    gc = pygsheets.authorize(service_account_info=st.secrets["gcp_service_account"])

sheet_url = "https://docs.google.com/spreadsheets/d/1wqAJBWdS3jncP455KcJ0qpbJgzhVplOVG-JM4u8MvJU/edit?gid=0"

# ----------------------- LEITURA DADOS PÁGINA 1 -----------------------
aba = gc.open_by_url(sheet_url).worksheet_by_title("Página1")
df = pd.DataFrame(aba.get_all_records())

# ----------------------- EXIBIR TABELA -----------------------
st.title("📊 Dados da Página 1")
st.dataframe(df, use_container_width=True)
