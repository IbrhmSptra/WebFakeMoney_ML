import pickle
import numpy as np
import pandas as pd
import streamlit as st
import re

#load model KNN from pickle
with open('modelKNN.pkl','rb') as file:
    modelKNN = pickle.load(file)

#create session dengan default value None untuk menampilkan hasil
if 'hasil' not in st.session_state:
        st.session_state['hasil'] = None

st.title("Web Pendeteksi Uang Palsu")
st.write("""Website ini akan mendeteksi uang anda palsu atau tidak (Dalam Dolar), dengan memasukan ciri ciri pada uang anda.
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
    submit = st.form_submit_button("Submit")
    if submit :
        #Ubah Ke Dictionary
        data = {
            "diagonal" : diagonal,
            "height_left" : height_left,
            "height_right" : height_right,
            "margin_low" : margin_low,
            "margin_up" : margin_up,
            "length" : length
        }
        #Ubah ke DataFrame
        data = pd.DataFrame(data, index=[0])
        #predict inputan dari user
        predict = modelKNN.predict(data)
        #ubah ke String
        predict = str(predict)
        # Clean string ['Asli'] -> Asli
        hasil = ''.join(re.findall(r'[a-zA-Z]', predict))
        #masukan ke session beserta kata nya
        st.session_state['hasil']= "Hasilnya Adalah : "+hasil
    #Seleksi jika asli tampilkan succses
    if st.session_state['hasil'] != None and st.session_state['hasil'] != "Hasilnya Adalah : Palsu":
        st.success(st.session_state['hasil'])
    #seleksi jika palsu tampilkan Erorr
    if st.session_state['hasil'] != None and st.session_state['hasil'] != "Hasilnya Adalah : Asli":
        st.error(st.session_state['hasil'])