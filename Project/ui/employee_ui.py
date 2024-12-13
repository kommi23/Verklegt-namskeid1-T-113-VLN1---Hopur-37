
class Employee_ui:

    def display_menu():
        print("\nEmployee Menu")
        print("1. List all employees")
        print("2. Search for employee")
        print("3. Available Maintenance Requests")
        print("4. Search for Maintenance Requests")
        print("0. Go back")

        choice = str(input("Enter your choice:"))
        valid_choices = ["1", "2", "3", "4", "0"]

        if choice not in valid_choices:
            print("Please enter a valid choice!")
            Employee_ui.display_menu

        elif choice == "1":
            Common_functions.display_employees()
            Employee_ui.display_menu()

        elif choice == "2":
            print("\nDo you want to:")
            print("1. Search for employee by ID ")
            print("2. Search for employee by Location ")

            choice = str(input("Enter your choice:"))

            if choice == "1":
                Common_functions.search_employee_by_id()
                Employee_ui.display_menu()


            elif choice == "2":
                Common_functions.search_employee_by_location()
                Employee_ui.display_menu()


        elif choice == "3":  
            Common_functions.display_maintenace_requests()
            Employee_ui.display_menu()

        elif choice == "4":
            Common_functions.search_maintenace_request_by_id()
            Employee_ui.display_menu()

        elif choice == "0":
            Mainmenu_ui.display_menu()


import os
from logic.logic_wrapper import *
from ui.common_functions_ui import *
from ui.main_ui import Mainmenu_ui