
class Manage_employees:
    def display_menu():
        # display choices
        print("\n==Employee Mananger Menu==")
        print("1. Create new employee")
        print("2. Search for employee")
        print("3. Change employee")
        print("0. Go back")

        choice = str(input("Enter your choice:"))

        # set up valid choices to catch some errors
        valid_choices = ["1","2","3","0"]
        if choice not in valid_choices:
            print("Please enter a valid choice!")
                
            Manage_employees.display_menu()

        # set up what the choices do
        if choice == "1":
            add_employee()
            return 
            
        if choice == "2":
            employee_search()
        
        if choice == "3":
             update_employee()

        if choice == "0":
            Manager_ui.display_menu()
             

def employee_search():
        # display choices of submenu
        print("\n == Employee mananger Search==")
        print("1. list all employees")
        print("2. search for employee by id")
        print("3. list all employees by location")
        print("0. Go back")

        choice = str(input("Enter your choice:"))
        valid_choices = ["1","2","3","0"]

        if choice not in valid_choices:
            print("Please enter a valid choice!")
            I_understand = None
            I_understand = input("Enter anything to continue")
            if I_understand != None:
                employee_search()()

        if choice not in valid_choices:
            print("Please enter a valid choice!")
    
        if choice == "1":
            Common_functions.display_employees()
            return employee_search()
        
        elif choice == "2": 
            employee = Common_functions.search_employee_by_id()
            if employee:
                print(employee)
            return employee_search()
        
        elif choice == "3":
            list_employees_by_location()
            return employee_search()

        elif choice == "0":
            Manage_employees.display_menu() 
               

def add_employee():
    list_of_locations = ["Nuuk", "Kulusuk", "Þórshöfn", "Tingwall", "Reykjavik"]
    id = None
    name = None
    email = None
    address = None
    work_phone = None
    personal_phone = None
    location = None

    while id == None or not id.isnumeric():
        id = input("ID: ")
        if not id.isnumeric() :
            print("Please enter a valid ID! ")

    while name == None:
            name = input("Name: ").lower()

    while email == None or email == "wrong":
        email = input("Email: ").lower()

        if "@" not in email:
             email = "wrong"
             print("Invalid email: Missing @ sign")

        elif "." not in email:
             email = "wrong"
             print("Invalid email: Missing .")
        
    while address == None:
        address = input("Address: ").lower()
        if address == None:
                print("Please Enter a valid address!")

    while work_phone == None or not work_phone.isnumeric():  
        work_phone = input("Work Phone: ")
    
        if not work_phone.isnumeric():
             print("Please enter a valid phone number (Use numbers only)")

    while personal_phone == None or not personal_phone.isnumeric():
        personal_phone = input("Personal Phone: ")

        if personal_phone.isnumeric() == False:
             print("Please enter a valid phone number (Use numbers only)")
        
    while location == None or location not in list_of_locations:
        if location == None or location not in list_of_locations:
            location = input("Location: ")
        if location not in list_of_locations:
             print("Not a valid location, please select one of: Nuuk, Kulusuk, Þórshöfn, Tingwall or Reykjavik")

    # Show all the information collected and prompt the user to confirm if its right
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"Work Phone: {work_phone}")
    print(f"Personal Phone: {personal_phone}")
    print(f"Location: {location}")
    print("Press 1. to confirm that the information is right, press anything else to restart: ")
    confirmation = int(input())

    if confirmation == 1:
        new_employee = Employee(id, name, email, address, work_phone, personal_phone, location)
        LL_employee.add_employee_lw(new_employee)
        return Manage_employees.display_menu()
    else:
         add_employee()
         
def update_employee():
        id = input("Enter the ID of the employee you want to update: ")
        info_change = input("Enter what information to update (e.g. name, location): ").lower()
        new_info = input("Enter new information: ")
        
        info_dict = {
            "name" : 1,
            "location" : 2,
            "phone_number" : 3,
            "email" : 4,
            "address" : 5
        }
        if info_change not in info_dict:
            print("Error: Information not found")
            return
        
        LL_employee.update_employee_lw(id, new_info, info_dict[info_change])
        print(f"Employee with ID {id} updated successfully")


def list_employees_by_location():
        
    #os.system("clear")
        
    allLocations = []
    allLocations = LL_location.list_all_locations()


    count : int = 0
    for emp in allLocations:
        if count == 0:
            pass
        else: 
            print ("    ", str(count), ") " , emp.location)
            
        count = count +1
    # end for 
    print ("    0) to Go back")
        
    try:
        location_search = int(input())
        if location_search == 0: 
            # Go back 
            return Manage_employees.display_menu()
    except ValueError: 
        print("Please entert a valid input") 
        return list_employees_by_location()
    

    selected = None 
    opt = int(location_search)
    
    try: 
        selected = allLocations[opt]
        employees = LL_employee.search_employee_location_lw(selected.location.strip())
    
        if len(employees) == 0:
            print("No employees found for this location: ", selected.location)
        for i in employees:
            print(i)    
        employee_search()
    except: 
        print("Please select a valid location")
        return list_employees_by_location()

import os
from ui.manager_ui import Manager_ui
from logic.logic_wrapper import *
from Models.Employee import Employee
from ui.common_functions_ui import Common_functions