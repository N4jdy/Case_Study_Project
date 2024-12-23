import streamlit as st

def show():
    st.title("Geräte-Verwaltung")

    st.header("Gerät anlegen")
    st.text_input("Name des Geräts")
    st.text_input("Verantwortliche Person")
    st.date_input("Anschaffungsdatum")
    st.button("Gerät hinzufügen")

    st.header("Gerät ändern")
    st.selectbox("Gerät auswählen", ["Laser-Cutter", "3D-Drucker", "Mikroskop"])
    st.text_input("Neuer Name")
    st.text_input("Neue verantwortliche Person")
    st.date_input("Neues Wartungsdatum")
    st.button("Gerät speichern")
