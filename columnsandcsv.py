import pandas as pd
import numpy as np
import streamlit as st

st.header("La peor App de la historia")

convertidor_coma_a_column = "Ingrese texto separado por comas"
convertidor_column_a_coma = "Ingrese texto en columnas separadas por salto de línea"

text_input_coma = st.text_input(convertidor_coma_a_column)
text_input_column = st.text_input(convertidor_column_a_coma)

if st.button("Convertir Texto"):
    if text_input_coma != "":
        result = convertidor_coma_a_column(text_input_coma)
        st.success("Texto convertido:")
        st.code(result, language='text')
    elif text_input_column != "":
        result = convertidor_column_a_coma(text_input_column)
        st.success("Texto convertido:")
        st.code(result, language='text')
    else:
        raise ValueError("Pusiste cualquier cosa Botardo")

def convertidor_coma_a_column(text):
    return "\n".join(text.split(", ")).strip()

def convertidor_column_a_coma(text):
    return ", ".join(text.splitlines())
