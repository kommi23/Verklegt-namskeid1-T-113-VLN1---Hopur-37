
class Employee_ui:
    def display_menu():
        print("kemst í mainemp")
        choice = None
        while choice != 0 or 1 or 2 or 3:
            print("#################################")
            print("           Employe Menu          ")
            print("#################################")
            print("1. Search employees              ")
            print("2. Open maintenance requests     ")
            print("3. Create a maintenance report   ")
            print("4. Return                        ")
            choice = int(input("Enter your choice: "))
            try:
                if choice == 1:
                    SearchEmployeeEmpUI.emp_search_menu()
                if choice == 2:
                    MaintenanceReuquestsUI.display_menu()
                if choice == 3:
                    MaintenanceReuquestsUI.display_menu()
             
                if choice == 4:
                    Mainmenu_UI.display_menu()
                else:
                    print("Invalid input. Please try again: ")
            
            except ValueError:
                print("Please enter an integer from 1 - 4: ")
                
                
from ui.manager_ui import *
from ui.main_ui import Mainmenu_UI
from ui.maintenance_requests_UI import MaintenanceReuquestsUI
from ui.employee_search_emp import *
from ui.maintenance_requests_UI import *