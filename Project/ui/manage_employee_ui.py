
class Manage_employees:
    def display_menu():
        # display choices
        print("1. Create new employee")
        print("2. Search for employee")
        print("3. Change employee")
        print("0. Go back")

        choice = input("Enter your choice:")

        # write all if choice
        if choice == 1:
            add_employee()
            
        elif choice == 2:
            # display choices of submenu
            print("1. list all employees")
            print("2. search for employee by id")
            print("3. list all employees by location")
            print("0. Go back")

            choice = input("Enter your choice:")
            
            # write all if choice
            if choice == 1:
                Common_functions.display_employees()
                Manage_employees.display_menu()
            
            if choice == 2: 
                Common_functions.search_employee_by_id()
                Manage_employees.display_menu()
            
            if choice == 3:
                list_employees_by_location()
                Manage_employees.display_menu()

            if choice == 0:
                 Manage_employees.display_menu()
            
            else:
                print("Enter a choice between 0-3")
                Manage_employees.display_menu()
                 
        if choice == 3:
             update_employee()
             Manage_employees.display_menu()

        if choice == 0:
             Manager_ui.display_menu()
             
             
             







def add_employee():
    #Get all locations
    all_locations = LL_location.list_all_locations()
    list_of_locations = []
    for location in all_locations:
        list_of_locations = location.location
    # Initiate variables
    id = None
    name = None
    email = None
    address = None
    work_phone = None
    personal_phone = None
    location = None
    # Do surface level check if input is allowed
    while id == None or not id.isnumeric():
        id = input("ID: ")
        if not id.isnumeric() :
            print("Please enter a valid ID! ")

    while name == None:
            name = input("Name: ").lower()

    while email == None:
        email = input("Email: ").lower()

        if "@" not in email:
             email = None
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
            location = input("Location: ")
            if location not in list_of_locations:
                print(f"Please enter one of these locations: {list_of_locations}")

    # Show all the information collected and prompt the user to confirm if its right
    print(f"ID: {id}")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Address: {address}")
    print(f"Work Phone: {work_phone}")
    print(f"Personal Phone: {personal_phone}")
    print(f"Location: {location}")
    print("Press 1. to confirm that the information is right, press anything else to restart: ")
    confirmation = str(input())

    if confirmation == "1":
        new_employee = Employee(id, name, email, address, work_phone, personal_phone, location)
        LL_employee.add_employee_lw(new_employee)

    # Restart loop if the user does not confirm
    else:
         add_employee()










def update_employee():
        # Collect information
        id = input("Enter the ID of the employee you want to update: ")
        info_change = input("Enter what information to update (e.g. name, location): ").lower()
        new_info = input("Enter new information: ")
        
        # List of information that is changeable and map to a number
        info_list = {

            "name" : 1,
            "location" : 2,
            "phone_number" : 3,
            "email" : 4,
            "address" : 5
        }
        # Check if info to be changed is in the map
        if info_change not in info_list:
            print("Error: Information not found")
            update_employee()
        # Send info down
        LL_employee.update_employee(id, new_info, info_list[info_change])
        print(f"Employee with ID {id} updated successfully")

        Manager_ui.display_menu


def list_employees_by_location():
    
    allEmployees = []
    allEmployees = LL_employee.get_employee_list_lw()

    count : int = 0
    for emp in allEmployees:
        if count == 0:
            pass
        else: 
            print ("    ", str(count), ") " , emp.location)
            
        count = count +1
    print ("    0) to Go back")
    location_search = int(input())
    opt = int(location_search)
    selected = None
    if opt == 0: 
        # Go back 
        return
    elif opt > len(allEmployees):
        # out of bounds of the array
        print("WTF!! ")
    else:
        selected = allEmployees[opt]

    employees = LL_employee.search_employee_location_lw(selected.location.strip())
    
    if len(employees) == 0:
        print("No employees found for this location: ", selected.location)
    for i in employees:
        print(i)    

    Manager_ui.display_menu()


from ui.manager_ui import Manager_ui
from logic.logic_wrapper import *
from Models.Employee import Employee
from ui.common_functions_ui import Common_functions