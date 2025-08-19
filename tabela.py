import streamlit as st
import pandas as pd
import pygsheets

sheet_url = "https://docs.google.com/spreadsheets/d/1wqAJBWdS3jncP455KcJ0qpbJgzhVplOVG-JM4u8MvJU/edit#gid=0"
aba_nome = "Página1"

# Pega as credenciais do Streamlit Cloud
credenciais_dict = st.secrets["gcp_service_account"]

# Autoriza usando service account
gc = pygsheets.authorize(service_account_info=credenciais_dict)

# Lê os dados
aba = gc.open_by_url(sheet_url).worksheet_by_title(aba_nome)
df = pd.DataFrame(aba.get_all_records())

st.title("📊 Dados da Página 1")
st.dataframe(df, use_container_width=True)
