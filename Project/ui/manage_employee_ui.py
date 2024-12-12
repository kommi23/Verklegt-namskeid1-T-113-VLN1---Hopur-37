
class Manage_employees:
    def display_menu():
        os.system("clear")

        print("1. Create new employee")
        print("2. Search for employee")
        print("3. Change employee")
        print("0. Go back")

        choice = int(input("Enter your choice:"))
        valid_choices = ["1","2","3","0"]

        if choice not in valid_choices:
            print("Please enter a valid choice!")
            I_understand = None
            I_understand = input("Enter anything to continue")
            if I_understand != None:
                Manage_employees.display_menu()

        if choice == 1:
            add_employee()
            
        elif choice == 2:
            print("1. list all employees")
            print("2. search for employee by id")
            print("3. list all employees by location")
            print("0. Go back")

            choice = int(input("Enter your choice:"))
            valid_choices = [1,2,3,0]

            if choice not in valid_choices:
                print("Please enter a valid choice!")
                I_understand = None
                I_understand = input("Enter anything to continue")
                if I_understand != None:
                    Manage_employees.display_menu()

            if choice not in valid_choices:
                 print("Please enter a valid choice!")
        
            if choice == 1:
                Common_functions.display_employees()
            
            elif choice == 2: #virkar
                search_employee_by_id()
            
            elif choice == 3:
                search_employee_by_location()

            elif choice == 0:
                 Manage_employees.display_menu()
                 
        if choice == 3:
             update_employee()

        if choice == 0:
             Manager_ui.display_menu()
             
             
             








        
def add_employee():
    list_of_locations = ["Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Reykjavik"]
    id = None
    name = None
    email = None
    address = None
    work_phone = None
    personal_phone = None
    location = None

    while True:
        if id == None or id.isnumeric() == False:
            id = input("ID: ")
        if id.isnumeric() == False:
            print("Please enter a valid ID! ")
        else:
             break

    while True:
        if name == None:
            name = input("Name: ").lower()
        if name:
             break
        
    while True:
        if email == None or email == "wrong":
            email = input("Email: ").lower()
        if "@" not in email:
             email = "wrong"
             print("Invalid email: Missing @ sign")
        elif "." not in email:
             email = "wrong"
             print("Invalid email: Missing .")
        else:
             break
        
    while True:
        if address == None:
            address = input("Address: ").lower()
        if address == None:
                print("Please Enter an address!")
        if address:
                break

    while True:
        if work_phone == None or work_phone.isnumeric() == False:    
            work_phone = input("Work Phone: ")
        if work_phone.isnumeric() == False:
             print("Please enter a valid phone number (Use numbers only)")
        else:
             break
    
    while True:
        if personal_phone == None or personal_phone.isnumeric() == False:
            personal_phone = input("Personal Phone: ")
        if personal_phone.isnumeric() == False:
             print("Please enter a valid phone number (Use numbers only)")
        else:
             break
        
    while True:
        if location == None or location not in list_of_locations:
            location = input("Location: ")
        if location not in list_of_locations:
             print("Not a valid location, please select one of: Nuuk, Kulusuk, Þórshöfn, Tingwall or Reykjavik")
        else:
             break

    os.system("clear")
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"Work Phone: {work_phone}")
    print(f"Personal Phone: {personal_phone}")
    print(f"Location: {location}")
    print("Press 1. to confirm that the information is right: ")
    confirmation = int(input())

    if confirmation == 1:
        new_employee = Employee(id, name, email, address, work_phone, personal_phone, location)
        LL_employee.add_employee_lw(new_employee)



def update_employee():
        id = input("Enter the ID of the employee you want to update: ")
        info_change = input("Enter what information to update (e.g. name, location): ").lower()
        new_info = input("Enter new information: ")
        
        info_list = {

            "name" : 1,
            "location" : 2,
            "phone_number" : 3,
            "email" : 4,
            "address" : 5
        }
        if info_change not in info_list:
            print("Error: Information not found")
            return
        
        print("Komumst í info change")
        LL_employee.update_employee(id, new_info, info_list[info_change])
        print(f"Employee with ID {id} updated successfully")

def search_employee_by_name():


        name = input("Enter Employee Name to search: ")
        employee = LL_employee.search_employee_name(name)
        if not employee:
            print("No Employee found with name {name}.")
        
        else:
            table = [[employee["id"], employee["name"], employee["location"], employee["phone_number"], employee["email"], employee["address"]]]
            #print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
# Komið í Common_functions
def search_employee_by_id(): #virkar
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
        employees = LL_employee.search_employee_location(location)
        if not employees:
            print("No employees found in location {location}.")
        
        else:
            for i in employees:

                print(i)

import os

from ui.manager_ui import Manager_ui

from logic.logic_wrapper import *

from Models.Employee import Employee

from ui.common_functions_ui import Common_functions