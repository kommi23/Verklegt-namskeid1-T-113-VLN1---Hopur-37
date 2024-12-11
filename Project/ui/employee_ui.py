#import os
from logic.logic_wrapper import *
from logic.employee_logic import *
from Models.Employee import *
class EmployeeUI:
    def employee_menu(self):
        #os.system("clear")

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
            employee = LL_employee.get_employee_list()
            if not employee:
                print("No employees found...")
                return
            else:
                table = [
                    [emp['id'], emp['name'], emp['location'], emp['gsm'], emp['address'], emp['opening_hours']]
                    for emp in employee
                    ]
                print(table)
    	


    def search_employee_by_name():
        name = input("Enter Employee Name to search: ")
        employee = LL_employee.logic.search_employee_name(name)
        if not employee:
            print("No Employee found with name {name}.")
        
        else:
            table = [[employee["id"], employee["name"], employee["location"], employee["phone_number"], employee["email"], employee["address"]]]
            #print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))

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
            #print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))




#def search_employee():
        #