import streamlit as st

def main():
   # Anmeldung
   if "user_logged_in" not in st.session_state:
      st.session_state["user_logged_in"] = False
      st.session_state["role"] = None
      st.session_state["name"] = None
      st.session_state["email"] = None
      st.session_state["passwort"] = None

   if not st.session_state["user_logged_in"]:
      with st.form("login_form"):
         st.subheader("Anmeldung")
         role = st.radio("Bitte wählen Sie Ihre Rolle:", ["Administrator", "Nutzer"])
         name = st.text_input("Name")
         email = st.text_input("Email")
         passwort = st.text_input("Passwort")
         submitted = st.form_submit_button("Anmelden")

         if submitted:
            if role and name and email and passwort:
               st.session_state["user_logged_in"] = True
               st.session_state["role"] = role
               st.session_state["name"] = name
               st.session_state["email"] = email
               st.session_state["passwort"] = passwort
               st.rerun()
            else:
               st.error("Bitte füllen Sie alle Felder aus.")
      
   if st.session_state["user_logged_in"]:
      if st.sidebar.button("Abmelden / Rolle wechseln"):
         st.session_state["user_logged_in"] = False
         st.session_state["role"] = None
         st.session_state["name"] = None
         st.session_state["email"] = None
         st.rerun()
   
   if not st.session_state["user_logged_in"]:
      st.stop()

   st.title("Geräteverwaltungssystem")

   # Seitenoptionen abhängig von der Rolle
   if st.session_state["role"] == "Administrator":
      menu = ["Startseite", "Nutzer-Verwaltung", "Geräte-Verwaltung", "Reservieungssystem", "Wartungsmanagment"]
   else:
      menu = ["Startseite", "Geräte-Übersicht"]

   #choice = st.sidebar.selectbox("Navigationsmenü", menu)
   choice = st.sidebar.radio("Navigationsmenü", menu)

   if st.session_state["role"] == "Administrator":
      if choice == "Startseite":
         st.subheader("Willkommen zum Geräteverwaltungssystem")
         st.write("Verwalten Sie Geräte, Reservierungen, Wartungen und Nutzer auf einfache Weise.")
         startseite()

      if choice == "Nutzer-Verwaltung":
         st.subheader("Nutzer-Verwaltung")
         manage_users()

      elif choice == "Geräte-Verwaltung":
         st.subheader("Geräte-Verwaltung")
         manage_devices()

      elif choice == "Reservieungssystem":
         st.subheader("Reservieungssystem")
         handle_reservations()


      elif choice == "Wartungsmanagment":
         st.subheader("Wartungsmanagment")
         handle_maintenence()

   elif st.session_state["role"] == "Nutzer":
      if choice == "Startseite":
         st.subheader("Willkommen zum Geräteverwaltungssystem")
         st.write("Reservieren sie die Geräte auf einfache Weise.")
         startseite()

      if choice == "Geräte-Übersicht":
         st.subheader("Geräte-Übersicht")
         view_devices()
   
   class user:
      pass
   class device: # -> def get_device_data() als Klasse abbilden
      pass


def startseite():
   last_role = st.session_state["role"]
   last_name = st.session_state["name"]
   last_email = st.session_state["email"]
   last_passwort = st.session_state["passwort"]

   st.success("Erfolgreich eingeloggt!")
   st.write("Angemeldet als:")
   container = st.container(border=True)
   container.write(f"{last_role}")
   container.write(f"Name: {last_name}")
   container.write(f"Email: {last_email}")
   #container.write(f"Passwort: {last_passwort}")
   

def manage_users():
   """Funktion für die Nutzerverwaltung."""
   menu = ["Nutzer anlegen", "Nutzer anzeigen"]
   user_choice = st.radio("Optionen", menu)

   if user_choice == "Nutzer anlegen":
      st.subheader("Neuen Nutzer anlegen")
      with st.form("user_form"):
         username = st.text_input("Benutzername")
         email = st.text_input("E-Mail-Adresse")
         role = st.selectbox("Rolle", ["Administrator", "Nutzer"])
         submitted = st.form_submit_button("Speichern")

         if submitted:
               st.success(f"Nutzer {username} wurde erfolgreich angelegt!")

   elif user_choice == "Nutzer anzeigen":
      st.subheader("Bestehende Nutzer anzeigen")
      st.write("[Platzhalter: Liste der Nutzer]")


def manage_devices():
   """Funktion für die Geräteverwaltung durch Administratoren."""
   rooms = get_device_data()

   tabs = st.tabs(list(rooms.keys()))

   for tab, (room, devices) in zip(tabs, rooms.items()):
      with tab:
         st.subheader(room)
         for device, description in devices:
               col1, col2 = st.columns([1, 3])
               with col1:
                  st.image(f"https://via.placeholder.com/150", caption=device, use_container_width=True)
               with col2:
                  st.write(f"**{device}**")
                  st.write(description)
               st.button(f"Gerät bearbeiten ({device})")


def view_devices():
    """Funktion für die Geräteübersicht für Nutzer."""
    rooms = get_device_data()

    tabs = st.tabs(list(rooms.keys()))

    for tab, (room, devices) in zip(tabs, rooms.items()):
        with tab:
            st.subheader(room)
            for device, description in devices:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(f"https://via.placeholder.com/150", caption=device, use_container_width=True)
                with col2:
                    st.write(f"**{device}**")
                    st.write(description)
                if st.button(f"Gerät reservieren ({device})"):
                    st.success(f"Reservierung für {device} wurde erfolgreich eingetragen!")


def get_device_data():
    """Gerätedaten als Dictionary."""
    return {
        "Werkstatt": [
            ("Laser-Cutter", "Für präzise Schnitte in Holz, Kunststoff oder Metall."),
            ("3D-Drucker", "Für Prototypen und Modellbau."),
            ("CNC-Fräsmaschinen", "Für computergesteuerte Bearbeitung von Werkstoffen."),
            ("Schweißgeräte", "Für Metallarbeiten und Fertigung."),
            ("Plotter", "Für großformatige Drucke und Schablonen."),
            ("Textilpressen", "Für das Bedrucken von Textilien."),
            ("Sägen und Bohrmaschinen", "Stationär und mobil.")
        ],
        "Labor": [
            ("Mikroskope", "Licht- und Elektronenmikroskope."),
            ("Spektrometer", "Für chemische und physikalische Analysen."),
            ("Oszilloskope", "Für die Signalüberwachung in der Elektronik."),
            ("3D-Scanner", "Zur Digitalisierung von Objekten."),
            ("Pipettierroboter", "Für Laborarbeiten in der Biologie oder Chemie."),
            ("Lötstationen", "Für Elektronikprojekte.")
        ],
        "Medienstudio": [
            ("Kameras", "Für Fotografie und Filmproduktion."),
            ("VR/AR-Headsets", "Für interaktive Anwendungen und Simulationen."),
            ("Drohnen", "Für Luftaufnahmen und Forschung."),
            ("Beleuchtungstechnik", "Für Film- und Medienstudios."),
            ("Mischpulte und Audio-Interfaces", "Für Tonproduktion.")
        ],
        "IT-Labor": [
            ("Computer-Arbeitsstationen", "Mit spezialisierter Software wie CAD oder GIS."),
            ("Server und NAS-Systeme", "Für die Verwaltung von Daten und Netzwerken."),
            ("Render-Farmen", "Für grafikintensive Projekte wie Animation."),
            ("Tablets und Grafik-Tablets", "Für digitale Kunst und Design."),
            ("VR-Labs", "Vollständige Workstations für immersive Anwendungen.")
        ],
        "Technische Einrichtungen": [
            ("Robotik-Arbeitsplätze", "Mit Roboterarmen oder mobilen Robotern."),
            ("Windkanäle", "Für aerodynamische Untersuchungen."),
            ("Simulationsanlagen", "Für Ingenieur- oder Verkehrsmodelle."),
            ("Hydraulik- und Pneumatik-Systeme", "Für technische Studien.")
        ],
        "Infrastruktur": [
            ("Projektoren und Whiteboards", "Für Vorlesungen und Seminare."),
            ("Drucker und Scanner", "Standard und großformatig."),
            ("Smartboards und interaktive Displays", "Für modernste Präsentationen.")
        ]
    }


def handle_reservations():
   pass


def handle_maintenence():
   pass


if __name__ == "__main__":
    main()



_ = """
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
"""