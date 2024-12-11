import os
from logic.logic_wrapper import *
from Models.Employee import *
class Manage_employees:
    def display_menu():
        os.system("clear")

        print("1. Create new employee")
        print("2. Search for employee")
        print("3. Change employee")

        choice = int(input("Enter your choice:"))

        if choice == 1:
            add_employee()
            
        elif choice == 2:
            print("1. list all employees")
            print("2. search for employee by name")
            print("3. search for employee by id")
            print("4. search for employee by location")

            user_input = int(input("Enter your choice:"))
        
            if user_input == 1:
                display_employees()

            elif user_input == 2:
                search_employee_by_name()
            
            elif user_input == 3: #virkar
                search_employee_by_id()
            
            elif user_input == 4:
                search_employee_by_location()
             
             




    
def display_employees():
    while True:
            employees = LL_employee.get_employee_list()
            
            # make list from emploeeys in tabulate form
            table = [
                [emp["id"], emp["name"], emp["location"], emp["phone_number"], emp["email"], emp["address"]]
                for emp in employees
            ]
            #print(tabulate(table, headers=["ID", "Name","Location", "Phone Number", "Email", "Address"], tablefmt="grid"))

        
def add_employee():
    fields = ["ID", "Name", "Email", "Address", "Work Phone", "Personal Phone", "Location"]
    user_inputs = {}
    
    for field in fields:
        os.system("clear")

        for key, value in user_inputs.items():
            print(f"{key}: {value}")
        
        print(f"{field}: ", end="")
        user_inputs[field] = input()
    
    os.system("clear")
    for key, value in user_inputs.items():
        print(f"{key}: {value}")

    print("Press 1. to confirm that the information is right: ")
    confirmation = int(input())

    if confirmation == 1:
        new_employee = Employee(user_inputs["ID"], user_inputs["Name"], user_inputs["Email"], user_inputs["Address"], user_inputs["Work Phone"], user_inputs["Personal Phone"], user_inputs["Location"])
        LL_employee.add_employee(new_employee)



def update_employee():
        id = input("Enter Employee ID to update: ")
        info_change = input("Enter what information to update (e.g. name, location): ").lower()
        new_info = input("Enter new information: ")
        
        info_list = {

            "name" : 1,
            "location" : 2,
            "phone_number" : 3,
            "email" : 4,
            "address" : 5
        }

        print(info_list[info_change])

        if info_change not in info_list:
            print("Error: Information not found")
            return
        
        print("Komumst í info change")
        LL_employee.update_employee(id, new_info, info_list[info_change])
        print(f"Employee with ID {id} updated successfully")
"""
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

"""