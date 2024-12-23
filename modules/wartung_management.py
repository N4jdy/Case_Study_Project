import streamlit as st

def show():
    st.title("Wartungs-Management")

    st.header("Wartungen anzeigen")
    wartungen = [
        {"Gerät": "Laser-Cutter", "Nächstes Wartungsdatum": "2024-12-30"},
        {"Gerät": "3D-Drucker", "Nächstes Wartungsdatum": "2025-01-15"}
    ]
    st.table(wartungen)

    st.header("Wartungskosten anzeigen")
    kosten = [
        {"Gerät": "Laser-Cutter", "Kosten pro Quartal": "100 €"},
        {"Gerät": "3D-Drucker", "Kosten pro Quartal": "150 €"}
    ]
    st.table(kosten)
