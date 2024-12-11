

class Mainmenu_UI:
    def display_menu():
                os.system("clear")
                print("####################")
                print("      Main Menu     ")
                print("####################")
                print("1. Employee")
                print("2. Manager")
                print("4. Contractor")
                print("0. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                     Employee_ui.display_menu()
                elif choice == '2':
                    Manager_ui.display_menu()
                elif choice == '3':
                      MaintenanceReuquestsUI.display_menu()
                elif choice == '0':
                      pass
                
from ui.manager_ui import *
from ui.employee_ui import *
from ui.emp_maintenance_report_ui import *
import os