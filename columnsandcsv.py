import pandas as pd
import numpy as np
import streamlit as st
import re

st.header(":rainbow::rainbow: La peor App de la historia :rainbow::rainbow:")

convertidor_coma_a_column = "Ingrese texto delimitado por comas"
convertidor_column_a_coma = "Ingrese texto en columnas"

text_input_coma = st.text_input(convertidor_coma_a_column)
text_input_column = st.text_input(convertidor_column_a_coma, value='', type='default')

def convertidor_coma_a_column(text):
    if re.search(r',\s*|\s*,\s*', text):
        return "\n".join(re.split(r',\s*|\s*,\s*', text)).strip()
    else:
        st.error(":ghost: Pusiste cualquier cosa Botardo :ghost:")

def convertidor_column_a_coma(text):
    # Primero, dividimos el texto en líneas
    lines = text.split('\n')
    # Verificamos si hay líneas con valores separados por espacios
    if any(re.search(r'\s+', line) for line in lines):
        # Si hay líneas con valores separados por espacios, reemplazamos los espacios por comas
        lines = [",".join(line.split()) for line in lines]
    # Verificamos si hay líneas con valores separados por comas
    if any(re.search(r',\s*', line) for line in lines):
        st.error(":ghost: Pusiste cualquier cosa Botardo :ghost:")
    else:
        return ", ".join(lines)

if st.button(":hot_pepper: Convertir Texto :hot_pepper:"):
    if text_input_coma:
        result = convertidor_coma_a_column(text_input_coma)
        if result:
            st.success("Texto convertido:")
            st.code(result, language='python')
    elif text_input_column:
        result = convertidor_column_a_coma(text_input_column)
        if result:
            st.success("Texto convertido:")
            st.code(result, language='python')
    else:
        st.error(":ghost: Pusiste cualquier cosa Botardo :ghost:")


