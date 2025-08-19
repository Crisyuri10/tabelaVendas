import streamlit as st
import pandas as pd
import os
import pygsheets

sheet_url = "https://docs.google.com/spreadsheets/d/1wqAJBWdS3jncP455KcJ0qpbJgzhVplOVG-JM4u8MvJU/edit#gid=0"
aba_nome = "Página1"

# ------------------------- DETECTA AMBIENTE -------------------------
if "CLOUD_ENV" in os.environ:  # flag fictícia para Streamlit Cloud
    # ------------------------- STREAMLIT CLOUD -------------------------
    conn = st.experimental_connection("gsheets", type="gsheets")
    df = conn.read(spreadsheet=sheet_url, worksheet=aba_nome)
else:
    # ------------------------- LOCAL -------------------------
    gc = pygsheets.authorize(service_file="cred.json")
    aba = gc.open_by_url(sheet_url).worksheet_by_title(aba_nome)
    df = pd.DataFrame(aba.get_all_records())

# ------------------------- EXIBIÇÃO -------------------------
st.title("📊 Dados da Página 1")
st.dataframe(df, use_container_width=True)



