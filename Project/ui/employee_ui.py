import os
from logic.logic_wrapper import *
from logic.employee_logic import *
from Models.Employee import *
from ui.common_functions_ui import *
from Models.Maintenance_request import *

class EmployeeUI:

    def display_menu():
        os.system("clear")


        print("\nEmployee Menu")
        print("1. List all employees")
        print("2. Search for employee")
        print("3. Available Maintenance Requests")
        print("4. Search for Maintenance Requests")
        print("5. Exit to main menu")


        choice = int(input("Enter your choice:"))


        if choice == 1:
            Common_functions.display_employees()

        elif choice == 2:
            print("1. Search Employee by ID")
            print("2. Search Employee by Location")
            
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                Common_functions.search_employee_by_id()
            elif user_input == 2:
                Common_functions.search_employee_by_location()

        elif choice == 3:  
            Common_functions.display_maintenace_requests()

        elif choice == 4:
            Common_functions.search_maintenace_request_by_id()

            
    def create_maintenance_report():
             
        
