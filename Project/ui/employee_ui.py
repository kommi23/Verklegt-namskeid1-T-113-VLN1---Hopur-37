
class Employee_ui:

    def display_menu():
        os.system("clear")


        print("\nEmployee Menu")
        print("1. List all employees")
        print("2. Search for employee")
        print("3. Available Maintenance Requests")
        print("4. Search for Maintenance Requests")
        print("5. Add Maintenance Report")
        print("6. Go back")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            Common_functions.display_employees()

        if choice == 2:
            print("\nDo you want to:")
            print("1. Search for employee by ID ")
            print("2. Search for employee by Location ")

            choice = int(input("Enter your choice:"))

            if choice == 1:
                Common_functions.search_employee_by_id()

            elif choice == 2:
                Common_functions.search_employee_by_location()

        if choice == 3:  
            Common_functions.display_maintenace_requests()

        if choice == 4:
            Common_functions.search_maintenace_request_by_id()

        if choice == 5:
            employee_write_maintenance_report()

        if choice == 6:
            Mainmenu_ui.display_menu()


import os
from logic.logic_wrapper import *
from ui.common_functions_ui import *
from ui.main_ui import Mainmenu_ui
from ui.manage_maintenances_ui import *