import streamlit as st

def show():
    st.title("Reservierungssystem")

    st.header("Reservierung eintragen")
    st.selectbox("Gerät auswählen", ["Laser-Cutter", "3D-Drucker", "Mikroskop"])
    st.date_input("Reservierungsdatum")
    st.text_input("Verwendungszweck")
    st.button("Reservierung hinzufügen")

    st.header("Reservierungen anzeigen")
    reservierungen = [
        {"Gerät": "Laser-Cutter", "Datum": "2024-12-25", "Nutzer": "Max Mustermann"},
        {"Gerät": "3D-Drucker", "Datum": "2024-12-26", "Nutzer": "Anna Müller"}
    ]
    st.table(reservierungen)
