import streamlit as st
import polars as pl
import sqlite3
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

st.markdown("# Emprestimos")
st.sidebar.markdown("# Emprestimos")

import os

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# For SQLite
db_path = os.path.join(BASE_DIR, "..", "data", "emprestimos_log.db")
conn = sqlite3.connect(db_path)
df_emprestimos_table = pl.read_database("select * from emprestimos_table", connection=conn)
db_path = os.path.join(BASE_DIR, "..", "data", "emprestimos_log.db")
conn = sqlite3.connect(db_path)
df_emprestimos_situacao = pl.read_database("select * from emprestimos_tudao", connection=conn)

if st.session_state["authentication_status"]:   
    st.dataframe(df_emprestimos_table, use_container_width=True, width=15000)
    st.write(df_emprestimos_table)
    st.markdown("## Emprestimos situação")
    st.dataframe(df_emprestimos_situacao, use_container_width=True, width=15000)
else:
    st.error('Você não está logado')