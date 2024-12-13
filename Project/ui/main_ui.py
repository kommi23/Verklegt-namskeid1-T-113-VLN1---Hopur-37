
class Mainmenu_ui:
    def display_menu():
        print("\nMain Menu")
        print("1. Employee")
        print("2. Manager")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Employee_ui.display_menu()
        if choice == 2:
            Manager_ui.display_menu()
        if choice == 0:
            quit()
        else: 
            print("Invalid choice, please select a 0-2")
            Mainmenu_ui.display_menu()


from ui.manager_ui import *
from ui.employee_ui import *
import os