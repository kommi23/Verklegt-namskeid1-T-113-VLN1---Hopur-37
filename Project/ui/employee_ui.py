from tabulate import tabulate
from logic.logic_wrapper import ll_employee
from Project.ui.input_validators import Input_validators

class EmployeeUI:
     
    def __init__(self):
        self.logic = ll_employee()

    def employee_menu(self):
        while True:    
            print("Employee Menu")
            print("1. Display Employees")
            print("2. Add Employee")
            print("3. Update Employee")
            print("4. Search Employee by name")
            print("5. Search Employee by ID")
            print("6. Search Employee by Location")
            print("7. Exit")


            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_employees()
            elif choice == '2':
                self.add_employee()
            elif choice == '3':
                self.update_employee()
            elif choice == '4':
                self.search_employee_by_name()
            elif choice == '5':
                self.search_employee_by_id()
            elif choice == '6':
                self.search_employee_by_location()
            elif choice == '7':
                print("Exiting to main menu")
                break
            else:
                print("Invalid choice, try again")


    
    def display_employees(self):
        while True:
            try:
                employees = self.logic.get_employee_list()
                
                # make list from emploeeys in tabulate form
                table = [
                    [emp["id"], emp["name"], emp["location"], emp["phone_number"], emp["email"], emp["address"]]
                    for emp in employees
                ]
                print(tabulate(table, headers=["ID", "Name","Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
                
            except Input_validators:
                print("some error") # added when input_val id finishid
            
    def add_employee(self):
        try:
            id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            location = input("Enter Employee Location: ")
            phone_number = input("Enter Employee Phone Number: ") # Vantar að bæta við heima/vinnusíma
            email = input("Enter Employee Email: ")
            address = input("Enter Employee Address: ")

            new_employee = self.logic.add_employee(id, name, location, phone_number, email, address)
            print(new_employee)
        except Input_validators:
            print("sonme error")
    
    def update_employee(self):
        try:
            id = input("Enter Employee ID to update: ")
            info_change = input("Enter what information to update (e.g. name, location): ").lower()
            new_info = input("Enter new {info_change}: ")
            
            info_list = {
                "name": 1,
                "location": 2,
                "phone_number": 3,
                "email": 4,
                "address": 5
            }

            if info_change not in info_list:
                print("Error: Information not found")
                return
            
            self.logic.update_employee(id, {info_change: new_info})
            print(f"Employee with ID {id} updated successfully")
        except Input_validators:
            print("Name was too long")

    def search_employee_by_name(self):
        try:
            name = input("Enter Employee Name to search: ")
            employee = self.logic.search_employee_name(name)
            if not employee:
                print("No Employee found with name {name}.")
            
            else:
                table = [[employee["id"], employee["name"], employee["location"], employee["phone_number"], employee["email"], employee["address"]]]
                print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
        except Input_validators:
            print("Name was too long")

    def search_employee_by_id(self):
            try:
                id = input("Enter Employee ID to search: ")
                employee = self.logic.search_employee_id(id)
                if not employee:
                    ("No employee found with the ID {id}.")
                
                else:
                    table = [[employee["id"], employee["name"], employee["location"], employee["phone_number"], employee["email"], employee["address"]]]
                    print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
            except Input_validators:
                print("Name was too long")

    def search_employee_by_location(self):
        try:
            location = input("Enter Employee Location to search from: ")
            employee = self.logic.search_employee_name(location)
            if not employee:
                print("No employees found in location {location}.")
            
            else:
                table = [[employee["id"], employee["name"], employee["location"], employee["phone_number"], employee["email"], employee["address"]]]
                print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
        except Input_validators:
            print("Name was too long")

