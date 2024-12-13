
class Employee_ui:
    def display_menu():
        # prompt the user with his valid choices
        print("\nEmployee Menu")
        print("1. List all employees")
        print("2. Search for employee")
        print("3. Available Maintenance Requests")
        print("4. Search for Maintenance Requests")
        print("5. Add Maintenance Report")
        print("0. Go back")

        choice = input("Enter your choice:")

        # if valid choices
        if choice == 1:
            Common_functions.display_employees()
            Employee_ui.display_menu()

        if choice == 2:
            print("\nDo you want to:")
            print("1. Search for employee by ID ")
            print("2. Search for employee by Location ")
            print("0. Go back")

            # if valid choices
            if choice == 1:
                Common_functions.search_employee_by_id()
                Employee_ui.display_menu()

            if choice == 2:
                Common_functions.search_employee_by_location()
                Employee_ui.display_menu()
            
            if choice == 0:
                Employee_ui.display_menu()
            
            else:
                print("Please select a number between 0-2")
                Employee_ui.display_menu()
            


        if choice == 3:  
            Common_functions.display_maintenace_requests()
            Employee_ui.display_menu()

        if choice == 4:
            Common_functions.search_maintenace_request_by_id()
            Employee_ui.display_menu()

        if choice == 5:
            employee_write_maintenance_report()

        if choice == 0:
            Mainmenu_ui.display_menu()


import os
from logic.logic_wrapper import *
from ui.common_functions_ui import *
from ui.main_ui import Mainmenu_ui
from ui.maintenance_ui import *