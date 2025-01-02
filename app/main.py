import streamlit as st
from utils.css import add_custom_css
from seiten import startseite, manage_users, manage_devices, view_devices, handle_reservations, handle_maintenance


st.set_page_config(
   page_title="Geräteverwaltungssystem", 
   page_icon="https://w7.pngwing.com/pngs/71/20/png-transparent-mci-management-center-innsbruck-university-of-innsbruck-master-s-degree-bachelor-s-degree-school.png", 
   layout="wide"
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
      menu = {
         "Startseite": startseite.display,
         "Nutzer-Verwaltung": manage_users.display,
         "Geräte-Verwaltung": manage_devices.display,
         "Reservierungssystem": handle_reservations.display,
         "Wartungsmanagement": handle_maintenance.display,
      }
   else:
      menu = {
         "Startseite": startseite.display,
         "Geräte-Übersicht": view_devices.display,
      }

   #choice = st.sidebar.selectbox("Navigationsmenü", list(menu.keys()))
   choice = st.sidebar.radio("Navigationsmenü", list(menu.keys()))

   if st.session_state["role"] == "Administrator":
      if choice == "Startseite":
         st.subheader("Willkommen zum Geräteverwaltungssystem")
         st.write("Verwalten Sie Geräte, Reservierungen, Wartungen und Nutzer auf einfache Weise.")
         startseite.display()

      if choice == "Nutzer-Verwaltung":
         st.subheader("Nutzer-Verwaltung")
         manage_users.display()

      elif choice == "Geräte-Verwaltung":
         st.subheader("Geräte-Verwaltung")
         manage_devices.display()

      elif choice == "Reservieungssystem":
         st.subheader("Reservieungssystem")
         handle_reservations.display()


      elif choice == "Wartungsmanagment":
         st.subheader("Wartungsmanagment")
         handle_maintenance.display()

   elif st.session_state["role"] == "Nutzer":
      if choice == "Startseite":
         st.subheader("Willkommen zum Geräteverwaltungssystem")
         st.write("Reservieren sie die Geräte auf einfache Weise.")
         startseite.display()

      if choice == "Geräte-Übersicht":
         st.subheader("Geräte-Übersicht")
         view_devices.display()
   
   class user:
      pass
   class device: # -> def get_device_data() als Klasse abbilden
      pass



if __name__ == "__main__":
    main()



