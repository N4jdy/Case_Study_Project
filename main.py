import streamlit as st

st.set_page_config(page_title="Geräteverwaltungssystem", page_icon="https://w7.pngwing.com/pngs/71/20/png-transparent-mci-management-center-innsbruck-university-of-innsbruck-master-s-degree-bachelor-s-degree-school.png", layout="wide")
def add_custom_css():
    st.markdown(
        """
        <style>
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
   add_custom_css()
   with st.sidebar:
        st.image("https://prod5.assets-cdn.io/event/5509/assets/8366056178-8d14582d14.png", use_container_width=True)
        st.markdown("---")
        st.markdown("### Kontakt")
        st.markdown("📧 Email: support@mci4me.at")
        st.markdown("📞 Telefon: +43 123 456 7890")
        

   
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
         for device, description, image in devices:
               col1, col2 = st.columns([1, 3])
               with col1:
                  st.image(image, caption=device, use_container_width=True)
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
            for device, description, image in devices:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(image, caption=device, use_container_width=True)
                with col2:
                    st.write(f"**{device}**")
                    st.write(description)
                if st.button(f"Gerät reservieren ({device})"):
                    st.success(f"Reservierung für {device} wurde erfolgreich eingetragen!")


def get_device_data():
    """Gerätedaten als Dictionary."""
    return {
        "Werkstatt": [
            ("Laser-Cutter", "Für präzise Schnitte in Holz, Kunststoff oder Metall.", "https://www.gettingsmart.com/wp-content/uploads/2016/10/Laser-Cutting-Technology-Feature-Image.jpg"),
            ("3D-Drucker", "Für Prototypen und Modellbau.", "https://www.zukunftsinstitut.de/hubfs/Imported_Blog_Media/03_Industrie4_0_flickr_Creative_Tools_3_CC-BY-SA-2_0-1.jpg"),
            ("CNC-Fräsmaschinen", "Für computergesteuerte Bearbeitung von Werkstoffen.", "https://www.techpilot.com/wp-content/uploads/2019/06/cnc-fraesen.jpg"),
            ("Schweißgeräte", "Für Metallarbeiten und Fertigung.", "https://www.hdb-schweiss-shop.de/images/product_images/popup_images/12167_5.jpg"),
            ("Plotter", "Für großformatige Drucke und Schablonen.", "https://ictnetcom.ch/wp-content/uploads/2018/12/grossformat_plotter.jpg"),
            ("Textilpressen", "Für das Bedrucken von Textilien.", "https://m.media-amazon.com/images/I/71qP8TnXPZL._AC_UF894,1000_QL80_.jpg"),
            ("Sägen und Bohrmaschinen", "Stationär und mobil.", "https://m.media-amazon.com/images/I/61bVJHxBShL.jpg")
        ],
        "Labor": [
            ("Mikroskope", "Licht- und Elektronenmikroskope.","https://www.kruess.com/wp-content/uploads/2024/07/Mikroskop-Monokular-Hellfeld-Abbe-Kondensor-Kruess_MML1200.jpg"),
            ("Spektrometer", "Für chemische und physikalische Analysen.", "https://katedry.czu.cz/storage/194/5864_DSC_9109.jpg"),
            ("Oszilloskope", "Für die Signalüberwachung in der Elektronik.", "https://cdn-reichelt.de/bilder/web/xxl_ws/D100/RTM_3K_X4_01.png"),
            ("3D-Scanner", "Zur Digitalisierung von Objekten.", "https://cdn.myshoptet.com/usr/www.materialpro3d.cz/user/shop/big/145754_revopoint-mini-2-3d-scanner-premium-package-mini2-advanced-edition-30237-3.png?6650b6dc"),
            ("Pipettierroboter", "Für Laborarbeiten in der Biologie oder Chemie.", "https://www.integra-biosciences.com/sites/default/files/2018-01/assist-plus-pipetting-robot-serial-dilution.jpg"),
            ("Lötstationen", "Für Elektronikprojekte.", "https://www.pollin.de/media/dc/7b/34/1701796676/840054-1-loetstation-zd-931.jpg")
        ],
        
        "Technische Einrichtungen": [
            ("Robotik-Arbeitsplätze", "Mit Roboterarmen oder mobilen Robotern.", "https://lupadata.com/wp-content/uploads/2022/09/Robot_arm_1.jpg"),
            ("Windkanäle", "Für aerodynamische Untersuchungen.", "https://wttech.cz/app/uploads/2023/09/12026_V01_03@2x.png"),
        ],
        
    }


def handle_reservations():
   pass


def handle_maintenence():
   pass



if __name__ == "__main__":
    main()


