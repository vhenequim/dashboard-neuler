import streamlit as st
st.set_page_config(layout="wide")
st.markdown("# Dashboard Neuler")
st.sidebar.markdown("# Dashboard Neuler")


import sys
import polars as pl
import pandas as pd
from datetime import datetime, timedelta
import sqlite3

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Define paths and print them for debugging
path_BO_Master = os.path.join(BASE_DIR, "data", "MasterFIA.xlsm")
path_BO_FIC = os.path.join(BASE_DIR, "data", "FICFIA.xlsm")
path_BO_HSF = os.path.join(BASE_DIR, "data", "HSF.xlsm")

# For SQLite
db_path = os.path.join(BASE_DIR, "data", "emprestimos_log.db")
sheet_emprestimos = 'Emprestimos_teste'
sheet_controle = 'Controle'


# @st.cache_data
def load_data_master():
    df = pd.read_excel(path_BO_Master, sheet_name=sheet_controle, usecols='I:L', header=2)
    df.dropna(inplace=True)
    df_polars = pl.from_pandas(df)
    dataf = df_polars.with_columns(
        (abs(pl.col('Diferença')) < 5).alias('Está OK?')
    )
    dataf = dataf.rename({'Unnamed: 8': 'Diferença (%)'})
    return dataf

def load_data_fic():
    df = pd.read_excel(path_BO_FIC, sheet_name=sheet_controle, usecols='I:L', header=2)
    df.dropna(inplace=True)
    df_polars = pl.from_pandas(df)
    dataf = df_polars.with_columns(
        (abs(pl.col('Diferença')) < 5).alias('Está OK?')
    )
    dataf = dataf.rename({'Unnamed: 8': 'Diferença (%)'})
    return dataf

def load_data_hsf():
    df = pd.read_excel(path_BO_HSF, sheet_name=sheet_controle, usecols='I:L', header=2)
    df.dropna(inplace=True)
    df_polars = pl.from_pandas(df)
    dataf = df_polars.with_columns(
        (abs(pl.col('Diferença')) < 5).alias('Está OK?')
    )
    dataf = dataf.rename({'Unnamed: 8': 'Diferença (%)'})
    return dataf


st.write('## Master')

dataf_master = load_data_master()

st.dataframe(
    dataf_master,
    use_container_width=True,
    hide_index=True,
    height=600
)


dataf_fic = load_data_fic()
dataf_hsf = load_data_hsf()


# Create two columns for FIC and HSF
col1, col2 = st.columns(2)


with col1:
    st.write('## FIC')
    dataf_fic = load_data_fic()
    st.dataframe(
        dataf_fic,
        use_container_width=False,
        hide_index=True,
        height=600,
        width=1000
    )

with col2:
    st.write('## HSF')
    dataf_hsf = load_data_hsf()
    st.dataframe(
        dataf_hsf,
        use_container_width=False,
        hide_index=True,
        height=600,
        width=1000
    )
