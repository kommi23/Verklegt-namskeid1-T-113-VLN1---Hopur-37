class Manager_ui:
    def display_menu_ui():
        print("1. Manage Employees")
        print("2. Manage Properties")
        print("3. Manage maintainance requests")
        print("4. Manage Contractors")
        print("5. Locations")
        print("0. Return")
        choice = int(input("Enter your choice:"))

        if choice == 1:
            Manage_employees.display_menu()

        if choice == 2:
            pass

from ui.manage_employee_ui import *