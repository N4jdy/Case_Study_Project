import streamlit as st
from tinydb import TinyDB, Query
import os
from devices import Device
from datetime import datetime

# Set up the database connection
db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), encoding='utf-8', ensure_ascii=False)
reservations_table = db.table('reservations')

def display():
    st.title("Geräte-Übersicht")
    
    devices = Device.find_all()
    
    categories = {}
    for device in devices:
        category = device.category
        if category not in categories:
            categories[category] = []
        categories[category].append(device)

    tabs = st.tabs(list(categories.keys()))

    for i, (category, devices) in enumerate(categories.items()):
        with tabs[i]:
            st.subheader(category)
            for device in devices:
                st.write(f"**{device.device_name}**")
                st.image(device.image_url, use_container_width=True)
                st.write(f"**Beschreibung:** {device.description}")
                st.write(f"**Kategorie:** {device.category}")
                st.write(f"**Verwalter:** {device.managed_by_user_id}")
                
                with st.form(f"reservation_form_{device.device_name}"):
                    start_date = st.date_input("Startdatum", key=f"start_date_{device.device_name}")
                    end_date = st.date_input("Enddatum", key=f"end_date_{device.device_name}")
                    submit_button = st.form_submit_button(label="Reservieren")
                    
                    if submit_button:
                        if start_date > end_date:
                            st.error("Das Startdatum muss vor dem Enddatum liegen.")
                        else:
                            # Check for overlapping reservations
                            overlapping_reservations = reservations_table.search(
                                (Query().device_id == device.device_name) &
                                (
                                    (Query().start_date <= end_date.strftime("%d.%m.%Y")) &
                                    (Query().end_date >= start_date.strftime("%d.%m.%Y"))
                                )
                            )
                            if overlapping_reservations:
                                st.error("Das Gerät ist in diesem Zeitraum bereits reserviert. Bitte wählen Sie einen anderen Termin.")
                            else:
                                reservation = {
                                    "device_id": device.device_name,
                                    "start_date": start_date.strftime("%d.%m.%Y"),
                                    "end_date": end_date.strftime("%d.%m.%Y")
                                }
                                reservations_table.insert(reservation)
                                st.success("Reservierung erfolgreich!")
                