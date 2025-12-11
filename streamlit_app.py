import streamlit as st
import numpy as np
st.set_page_config(page_title="Solusi SPNL - Newton Raphson", layout="wide")
st.title("Solusi SPNL dengan Metode Newton–Raphson")
st.write("Masukkan fungsi non-linear dan parameter perhitungannya di bawah ini.")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Input Fungsi dan Parameter")

f1_input = st.text_input("Fungsi f1(x, y):","x**2 + y**2 - 25")
