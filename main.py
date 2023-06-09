import pickle
import numpy as np
import pandas as pd
import streamlit as st

#load model KNN from pickle
with open('modelKNN.pkl','rb') as file:
    modelKNN = pickle.load(file)

if 'hasil' not in st.session_state:
        st.session_state['hasil'] = None

st.title("Web Pendeteksi Uang Palsu")
st.write("""Website ini akan mendeteksi uang anda palsu atau tidak, dengan memasukan ciri ciri pada uang anda.
        Lengkapi data uang anda pada form di bawah dalam ukuran MiliMeter (mm)
         Website ini dapat mendeteksi uang palsu atau asli dengan akurasi 97%. Selamat Mencoba""")
with st.form("InputanUangUser", clear_on_submit=True) :
    st.header("Input Ciri-Ciri Uang")
    length = st.number_input("Panjang Uang", min_value=0)
    diagonal = st.number_input("Panjang Diagonal", min_value=0)
    height_left = st.number_input("Panjang Kiri", min_value=0)
    height_right = st.number_input("Panjang Kanan", min_value=0)
    margin_low = st.number_input("Margin Bawah",min_value=0)
    margin_up = st.number_input("Margin Atas", min_value=0)
    submit = st.form_submit_button("submitUang")
    if submit :
        data = {
            "diagonal" : diagonal,
            "height_left" : height_left,
            "height_right" : height_right,
            "margin_low" : margin_low,
            "margin_up" : margin_up,
            "length" : length
        }
        data = pd.DataFrame(data, index=[0])
        predict = modelKNN.predict(data)
        st.session_state['hasil']= predict
        st.experimental_rerun()
    if st.session_state['hasil'] != None :
        st.write("Hasilnya adalah",st.session_state['hasil'])