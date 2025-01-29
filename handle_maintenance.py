import streamlit as st
from tinydb import TinyDB, Query
import os
from devices import Device
from datetime import datetime, timedelta

# Set up the database connection
db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), encoding='utf-8', ensure_ascii=False)
maintenance_table = db.table('maintenance')

def display():
    devices = Device.find_all()
    
    for device in devices:
        st.subheader(f"Wartungskosten und -planung für {device.device_name}")

        with st.form(f"maintenance_form_{device.device_name}"):
            quarter = st.selectbox("Quartal", ["Q1", "Q2", "Q3", "Q4"], key=f"quarter_{device.device_name}")
            year = st.number_input("Jahr", min_value=2000, max_value=datetime.now().year, value=datetime.now().year, key=f"year_{device.device_name}")
            cost = st.number_input("Kosten (€)", min_value=0.0, format="%.2f", key=f"cost_{device.device_name}")
            submit_button = st.form_submit_button(label="Kosten hinzufügen")
            st.write(f"Quartal: {quarter}, Jahr: {year}, Kosten: {cost} €")
            
            if submit_button:
                maintenance_record = {
                    "device_id": device.device_name,
                    "quarter": quarter,
                    "year": year,
                    "cost": cost
                }
                maintenance_table.insert(maintenance_record)
                st.success(f"Wartungskosten für {device.device_name} wurden hinzugefügt.")
                st.rerun()
        
        st.subheader("Nächstes Wartungsdatum")
        maintenance_entry = maintenance_table.get(Query().device_id == device.device_name)
        if maintenance_entry and 'next_maintenance_date' in maintenance_entry:
            next_maintenance_date = maintenance_entry['next_maintenance_date']
            st.write(f"Nächstes Wartungsdatum: {next_maintenance_date}")
        else:
            next_maintenance_date = (datetime.now() + timedelta(days=90)).strftime("%d.%m.%Y")
            maintenance_table.upsert({'device_id': device.device_name, 'next_maintenance_date': next_maintenance_date}, Query().device_id == device.device_name)
            st.write(f"Nächstes Wartungsdatum: {next_maintenance_date}")
        try:
            next_maintenance_date_dt = datetime.strptime(next_maintenance_date, "%d.%m.%Y")
        except ValueError:
            next_maintenance_date_dt = datetime.strptime(next_maintenance_date, "%Y-%m-%d")
            
        new_maintenance_date = st.date_input("Neues Wartungsdatum", value=next_maintenance_date_dt, key=f"new_maintenance_date_{device.device_name}")
        if st.button("Wartungsdatum aktualisieren", key=f"update_maintenance_date_{device.device_name}"):
            maintenance_table.update({'next_maintenance_date': new_maintenance_date.strftime("%d.%m.%Y")}, Query().device_id == device.device_name)
            st.success(f"Nächstes Wartungsdatum für {device.device_name} wurde aktualisiert.")
            st.rerun()