"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import polars as pl
import sqlite3
import pandas as pd
import numpy as np
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

conn = sqlite3.connect("Y:\Cod_Neuler_Labs_Org\Rotinas Operacionais\Carteira\emprestimos\common\emprestimos_log.db")
df_emprestimos_table = pl.read_database("select * from emprestimos_table", connection=conn)


df_emprestimos_table

st.write(df_emprestimos_table)

st.dataframe(df_emprestimos_table)

@st.cache_data
def load_data():
    map_data = pd.DataFrame(
        np.random.randn(10000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    return map_data

map_data = load_data()

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

    import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'

