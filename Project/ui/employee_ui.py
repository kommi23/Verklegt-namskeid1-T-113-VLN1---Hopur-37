
class Employee_ui:
    def display_menu():
        print("\nEmployee Menu")
        print("1. List all employees")
        print("2. Search for employee")
        print("3. Available Maintenance Requests")
        print("4. Search for Maintenance Requests")
        print("5. Add Maintenance Report")
        print("0. Go back")

        choice = str(input("Enter your choice:"))

        valid_choices = ["1", "2", "3", "4", "5", "0"]

        if choice not in valid_choices:
            print("Please enter a valid choice!")
            I_understand = None
            I_understand = input("Enter anything to continue")
            if I_understand != None:
                Mainmenu_ui.display_menu()

        if choice == "1":
            Common_functions.display_employees()
            Employee_ui.display_menu()

        if choice == "2":
            print("\nDo you want to:")
            print("1. Search for employee by ID ")
            print("2. Search for employee by Location ")
            print("0. Go back")

            choice = str(input("Enter your choice:"))
            valid_choices = ["1", "2", "0"]

            if choice not in valid_choices:
                print("Please enter a valid choice!")
                I_understand = None
                I_understand = input("Enter anything to continue")
                if I_understand != None:
                    Mainmenu_ui.display_menu()

            if choice == "1":
                print("We get into search by id")
                Common_functions.search_employee_by_id()
                Employee_ui.display_menu()


            if choice == "2":
                Common_functions.search_employee_by_location()
                Employee_ui.display_menu()
            
            if choice == "0":
                Employee_ui.display_menu()


        if choice == "3":  
            Common_functions.display_maintenace_requests()
            Employee_ui.display_menu()

        if choice == "4":
            Common_functions.search_maintenace_request_by_id()
            Employee_ui.display_menu()

        if choice == "5":
            employee_write_maintenance_report()

        if choice == "6":
            Mainmenu_ui.display_menu()


import os
from logic.logic_wrapper import *
from ui.common_functions_ui import *
from ui.main_ui import Mainmenu_ui
from ui.maintenance_ui import *