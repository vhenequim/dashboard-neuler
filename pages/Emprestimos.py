import streamlit as st
import polars as pl
import sqlite3
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

st.markdown("# Emprestimos")
st.sidebar.markdown("# Emprestimos")

if st.button('Atualizar'):
    st.write('Atualizando...')
else:
    st.write('Atualizado')
import os

# Get the current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the base directory
path_BO_Master = os.path.join(BASE_DIR, "data", "MasterFIA.xlsm")
path_BO_FIC = os.path.join(BASE_DIR, "data", "FICFIA.xlsm")
path_BO_HSF = os.path.join(BASE_DIR, "data", "HSF.xlsm")

# For SQLite
db_path = os.path.join(BASE_DIR, "data", "emprestimos_log.db")
conn = sqlite3.connect(db_path)
df_emprestimos_table = pl.read_database("select * from emprestimos_table", connection=conn)

st.dataframe(df_emprestimos_table, use_container_width=True, width=15000)
st.write(df_emprestimos_table)
st.table(df_emprestimos_table)
