class Manager_ui:
    def display_menu():
        os.system("clear")

        print("1. Manage Employees")
        print("2. Manage Properties")
        print("3. Manage maintainance requests")
        print("4. Manage Contractors")
        print("5. Manage Locations")
        print("0. Return")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            Manage_employees.display_menu()

        if choice == 2:
            Manage_properties.display_menu()

from ui.manage_employee_ui import *
from ui.manage_properties_ui import *