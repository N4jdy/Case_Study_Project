import streamlit as st
import json
import os
from devices import Device

def display():
    #devices_db_file = os.path.join(os.path.dirname(__file__), 'database.json')
    #with open(devices_db_file, 'r', encoding='utf-8') as file:
        #devices_db = json.load(file)
    devices_db = Device.find_all()
    #st.write(devices_db)

    categories = {}
    for device in devices_db:
        category = device.category
        if category not in categories:
            categories[category] = []
        categories[category].append(device)

    # Aktuellen Zustand für das Bearbeiten eines Geräts speichern
    if "editing_device" not in st.session_state:
        st.session_state["editing_device"] = False
        st.session_state["editing_device_data"] = None

    if not st.session_state["editing_device"]:
        tabs = st.tabs(list(categories.keys()))

        for i, (category, devices) in enumerate(categories.items()):
            with tabs[i]:
                st.subheader(category)
                for device_info in devices:
                    device_name = device_info.device_name
                    managed_by_user_id = device_info.managed_by_user_id
                    description = device_info.description
                    image_url = device_info.image_url
                    
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.image(image_url, caption=device_name, use_container_width=True)
                    with col2:
                        st.write(f"**{device_name}**")
                        st.write(description)
                        st.write(managed_by_user_id)

                    if st.button(f"Bearbeiten ({device_name})", key=f"edit_{device_name}"):
                        change_to_editing(device_info)
                        st.rerun()
                        #st.session_state["editing_device"] = True
                        #st.session_state["editing_device_data"] = device_info
                        #st.write("DEBUG: Button gedrückt!")
                        #st.write(f"DEBUG: Gerät zum Bearbeiten: {device_info}")

    #st.write(f"DEBUG: Aktueller Bearbeitungszustand: {st.session_state["editing_device"]}")
    #st.write(f"DEBUG: Aktueller Bearbeitungszustand: {st.session_state["editing_device_data"]}")
    
    if st.session_state["editing_device"]:
        # st.write(f"Debug: {st.session_state["editing_device_data"]}")
        edit_device_form(st.session_state["editing_device_data"])


def change_to_editing(device_info):
    st.session_state["editing_device"] = True
    st.session_state["editing_device_data"] = device_info


def edit_device_form(device):
    """Zeigt ein Formular zum Bearbeiten eines Geräts an."""
    if st.session_state["editing_device"]:
        # Modal-ähnliches Verhalten: Formular wird in der Mitte der Seite angezeigt
        with st.form("edit_device_form"):
            st.header("Gerät bearbeiten")

            # Felder mit aktuellen Werten vorfüllen
            st.write("Zum hinzufügen eines neuen Geräts, einen anderen Gerätename eingeben.")
            new_device_name = st.text_input("Gerätename", value=device.device_name)
            new_description = st.text_area("Beschreibung", value=device.description)
            new_managed_by_user_id = st.text_input(
                "Verantwortlicher Benutzer-ID", value=device.managed_by_user_id
            )
            new_image_url = st.text_input("Bild-URL", value=device.image_url)

            # Buttons
            delete_button = st.form_submit_button("Gerät permanent Löschen") 
            cancel_button = st.form_submit_button("Abbrechen")
            save_button = st.form_submit_button(" Änderungen speichern")

            if save_button:
                # Hier die Datenbank oder Datenstruktur aktualisieren
                device.device_name = new_device_name
                device.description = new_description
                device.managed_by_user_id = new_managed_by_user_id
                device.image_url = new_image_url

                device.store_data()

                st.success(f"Gerät {new_device_name} erfolgreich aktualisiert!")

                # Bearbeitungsmodus beenden
                st.session_state["editing_device"] = False
                st.rerun()

            elif cancel_button:
                # Bearbeitungsmodus abbrechen
                st.session_state["editing_device"] = False
                st.rerun()

            elif delete_button:
                # Gerät löschen
                device.delete()
                st.success(f"Gerät '{device.device_name}' wurde gelöscht.")

                # Bearbeitungsmodus beenden und Seite neu laden
                st.session_state["editing_device"] = False
                st.rerun()
    

