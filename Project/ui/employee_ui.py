

class EmployeeUI:
    def employee_menu(self):
        

        print("\nEmployee Menu")
        print("1. List all employees")
        print("1. Search for employee")
        print("2. Available Maintenance Requests")
        print("3. Search for Maintenance Requests")
        print("4. Exit to main menu")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            pass 
    
    def display_employees():
            employee = ll_employee.get_employee_list()
            if not employee:
                print("No employees found...")
                return
            else:
                table = [
                    [emp['id'], emp['name'], emp['location'], emp['gsm'], emp['address'], emp['opening_hours']]
                    for emp in employee
                    ]
                print(table)
    	
    def search_employee():
        print("\n Searching for Employees") 
        print("1. Search Employee by Name")
        print("2. Search Employee by ID")
        print("3. Search Employee by Location")
         
        choice = int(input("Enter your choice: "))

        if choice == '1':
              search_employee_by_name()
        elif choice == '2':
             search_employee_by_id()
        elif choice == '3':
             search_employee_by_location()
             
    def available_maintenance_requests():
         

            
    	
import os
from logic.logic_wrapper import *
from logic.employee_logic import *
from Models.Employee import *
from manage_employee_ui import *







