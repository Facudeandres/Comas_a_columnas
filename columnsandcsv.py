import pandas as pd
import numpy as np
import streamlit as st

st.header(":rainbow::rainbow: La peor App de la historia :rainbow::rainbow:")

convertidor_coma_a_column = "Ingrese texto delimitado por comas"
convertidor_column_a_coma = "Ingrese texto en columnas"

text_input_coma = st.text_input(convertidor_coma_a_column)
text_input_column = st.text_input(convertidor_column_a_coma)

if st.button(":hot_pepper: Convertir Texto :hot_pepper:"):
    if text_input_coma != "":
        result = convertidor_coma_a_column(text_input_coma)
        st.success("Texto convertido:")
        st.code(result, language='python')
    elif text_input_column != "":
        result = convertidor_column_a_coma(text_input_column)
        st.success("Texto convertido:")
        st.code(result, language='python')
    else:
        raise ValueError(":ghost: Pusiste cualquier cosa Botardo :ghost:")

def convertidor_coma_a_column(text):
    return "\n".join(text.split(", ")).strip()

def convertidor_column_a_coma(text):
    return ", ".join(text.splitlines())
