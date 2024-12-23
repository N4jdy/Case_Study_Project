import streamlit as st
from modules import gerate_verwaltung, reservierungssystem, wartung_management

# Setzt das Seitenlayout
st.set_page_config(page_title="Geräteverwaltung", layout="wide")

# Seiten-Navigation in der Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Wähle eine Seite:",
    ["Geräte-Verwaltung", "Reservierungssystem", "Wartungs-Management"]
)

# Lade das entsprechende Modul basierend auf der Auswahl
if page == "Geräte-Verwaltung":
    gerate_verwaltung.show()
elif page == "Reservierungssystem":
    reservierungssystem.show()
elif page == "Wartungs-Management":
    wartung_management.show()
