import pandas as pd
import numpy as np
import streamlit as st
import re

# Definir la constante TEXT_BOX_HEIGHT
TEXT_BOX_HEIGHT = 5 * 22

# Configurar la página
st.set_page_config(page_title="Conversor de texto",
                   page_icon=":pencil:",
                   layout="wide")

# Definir los cuadros de texto
st.sidebar.header("Conversor de texto")
text_input_coma = st.sidebar.text_input("Ingrese texto delimitado por comas", height=TEXT_BOX_HEIGHT)
text_input_column = st.sidebar.text_area("Ingrese texto en columnas", height=TEXT_BOX_HEIGHT)

# Definir las funciones de conversión
def convertidor_coma_a_column(text):
    if ',' in text:
        return "\n".join(text.split(", ")).strip()
    else:
        raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")

def convertidor_column_a_coma(text):
    lines = text.splitlines()
    if any(',' in line for line in lines):
        raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")
    return ", ".join(lines)

# Definir el botón de conversión
if st.button(":hot_pepper: Convertir Texto :hot_pepper:"):
    if text_input_coma:
        result = convertidor_coma_a_column(text_input_coma)
        st.success("Texto convertido:")
        st.code(result, language='python')
    elif text_input_column:
        try:
            result = convertidor_column_a_coma(text_input_column)
            st.success("Texto convertido:")
            st.code(result, language='python')
        except ValueError as e:
            st.error(str(e))
    else:
        raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")

