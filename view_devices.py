import streamlit as st
import json
import os
from devices import Device

def display():
    #"""Funktion für die Geräteübersicht für Nutzer."""
    #devices_db_file = os.path.join(os.path.dirname(__file__), 'database.json')
    #with open(devices_db_file, 'r', encoding='utf-8') as file:
        #devices_db = json.load(file)
    devices_db = Device.find_all()
  

    categories = {}
    for device in devices_db:
        category = device.category
        if category not in categories:
            categories[category] = []
        categories[category].append(device)

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
                if st.button(f"Gerät reservieren ({device_name})"):
                    st.success(f"Gerät {device_name} reserviert.")

