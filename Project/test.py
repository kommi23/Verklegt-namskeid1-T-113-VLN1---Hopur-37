from ui.main_ui import Mainmenu_ui
try: 
    Mainmenu_ui.display_menu()
except Exception:
    print("Something unexpected went wrong. You have been put back into the Main Menu")
    Mainmenu_ui.display_menu()

