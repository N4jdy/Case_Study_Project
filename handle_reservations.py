import streamlit as st
from tinydb import TinyDB, Query
import os
from datetime import datetime
from devices import Device

# Datenbankverbindung
db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'),encoding='utf-8', ensure_ascii=False )
reservations_table = db.table('reservations')

def display():
    st.title("Reservierungssystem")
    
    devices = Device.find_all()
            
    st.subheader("Bestehende Reservierungen")
    for device in devices:
        st.write(f"Reservierungen für Gerät: {device.device_name}")
        device_reservations = reservations_table.search(Query().device_id == device.device_name)
        if device_reservations:
            for res in device_reservations:
                st.write(f"- Von {res['start_date']} bis {res['end_date']}")
                if st.button(f"Reservierung entfernen", key=f"remove_{res.doc_id}"):
                    reservations_table.remove(doc_ids=[res.doc_id])
                    st.success(f"Reservierung von wurde entfernt.")
                st.rerun
        else:
            st.write("- Keine Reservierungen")