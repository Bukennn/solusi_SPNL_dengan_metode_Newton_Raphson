import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(page_title="Solusi SPNL - Newton Raphson", layout="wide")
st.title("Solusi SPNL dengan Metode Newton–Raphson")
st.write("Masukkan fungsi non-linear dan parameter perhitungannya di bawah ini.")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Input Fungsi dan Parameter")

f1_input = st.text_input("Fungsi f1(x, y):","x**2 + y**2 - 25")
f2_input = st.text_input("Fungsi f₂(x, y):", "x - y - 1")
x0 = st.number_input("Tebakan Awal x₀:", value=1.0)
y0 = st.number_input("Tebakan Awal y₀:", value=1.0)
iter_max = st.number_input("Jumlah Iterasi Maksimum:", value=20)
eps = st.number_input("Toleransi Error (ε):", value=0.0001, format="%.6f")
tombol = st.button("Hitung Newton-Raphson")

def f1(x, y):
    return eval(f1_input, {"x": x, "y": y, "np": np})

def f2(x, y):
    return eval(f2_input, {"x": x, "y": y, "np": np})

def jacobian(x, y):
    h = 1e-5
    df1_dx = (f1(x + h, y) - f1(x, y)) / h
    df1_dy = (f1(x, y + h) - f1(x, y)) / h
    df2_dx = (f2(x + h, y) - f2(x, y)) / h
    df2_dy = (f2(x, y + h) - f2(x, y)) / h
    return np.array([[df1_dx, df1_dy],
                     [df2_dx, df2_dy]])

if tombol:
    hasil_iterasi = []
    x, y = x0, y0
  
    for i in range(int(iter_max)):

        J = jacobian(x, y)
        F = np.array([f1(x, y), f2(x, y)])

        try:
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            st.error("Jacobian singular. Tidak bisa melanjutkan iterasi.")
            break

        x_new = x + delta[0]
        y_new = y + delta[1]

        error = np.sqrt((x_new - x)**2 + (y_new - y)**2)

        hasil_iterasi.append([i + 1, x_new, y_new, error])

        x, y = x_new, y_new

        if error < eps:
            break
      with col2:
        st.subheader("📌 Hasil Perhitungan")

        st.success(f"""
        **Solusi Akhir Ditemukan:**
        - x = `{x}`
        - y = `{y}`
        - Error terakhir = `{error}`
        - Iterasi = `{len(hasil_iterasi)}`
        """)

        st.subheader("📊 Tabel Iterasi")
        df = pd.DataFrame(hasil_iterasi, columns=["Iterasi", "x", "y", "Error"])
        st.dataframe(df, use_container_width=True)
