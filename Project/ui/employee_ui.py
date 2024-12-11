import os
from logic.logic_wrapper import *
from logic.employee_logic import *
from Models.Employee import *
from ui.common_functions_ui import *

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

        
        







def search_employee_by_id():
        id = input("Enter Employee ID to search: ")
        employee = LL_employee.search_employee_id(id)
        if not employee:
            print("No employee found with the ID {id}.")
        
        else:
            employee = Employee.turn_employee_into_list(employee)
            #print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
            print(employee)


def search_employee_by_location():
    location = input("Enter Employee Location to search from: ")
    employee = LL_employee.logic.search_employee_name(location)
    if not employee:
        print("No employees found in location {location}.")
    
    else:
        table = [[employee["id"], employee["name"], employee["location"], employee["phone_number"], employee["email"], employee["address"]]]
        print(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid")


    

""""class Employee_ui:
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
from ui.maintenance_requests_UI import *"""


""""class SearchEmployeeEmpUI:
    def emp_search_menu():


        print("#########################")
        print("     Employee search     ")
        print("#########################")
        print("1. View all employees")
        print("2. search by name")
        print("3. seach by id")
        print("4. search by location")
        print("5. return")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                Manage_employees.display_employees()
            if choice == 2:
                Manage_employees.search_employee_by_name()
            if choice == 3:
                Manage_employees.search_employee_by_id()
            if choice == 4:
                Manage_employees.search_employee_by_location()
            if choice == 5:
                Employee_ui.display_menu()
            else:
                print("Invalid input. Please enter choices 1-5: ")
"""

"""class EmpMaintenanceReport:
def maintenance_report_menu():
        print("######################################")
        print("          Maintenance Reports         ")
        print("######################################")
        print("1. Create maintenance report")
        print("2. View maintenance reports history")
        print("3. Return")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            pass
        if choice == 2:
            pass
        if choice == 3:
            Employee_ui.display_menu()
        else:
            print("Invalid Input")
           
from ui.employee_ui import *

"""

"""class MaintenanceReuquestsUI:
    def display_menu():
        print("#########################")
        print("  Maintenance Requests  " )
        print("#########################")
        print("1. view maintenance requests")
        print("2. search maintenance requests")
        print("3. Return")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                pass
            if choice == 2:
                pass
            if choice == 3:
                Employee_ui.display_menu()

                 else:
                print("Invalid input")
       
        except ValueError:
            print("Please enter an integer between 1 - 3: ")

"""

"""class SearchEmployeeEmpUI:
    def emp_search_menu():


        print("#########################")
        print("     Employee search     ")
        print("#########################")
        print("1. View all employees")
        print("2. search by name")
        print("3. seach by id")
        print("4. search by location")
        print("5. return")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                Manage_employees.display_employees()
            if choice == 2:
                Manage_employees.search_employee_by_name()
            if choice == 3:
                Manage_employees.search_employee_by_id()
            if choice == 4:
                Manage_employees.search_employee_by_location()
            if choice == 5:
                Employee_ui.display_menu()
            else:
                print("Invalid input. Please enter choices 1-5: ")
"""
