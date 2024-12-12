class Manager_ui:
    def display_menu():
        os.system("clear")

        print("1. Manage Employees")
        print("2. Manage Properties")
        print("3. Manage maintainance requests")
        print("4. Manage Contractors")
        print("5. Show all locations")
        print("0. Go back")

        choice = int(input("Enter your choice:"))
        valid_choices = [1, 2, 3, 4, 5, 0]
        
        if choice not in valid_choices:
            print("Please enter a valid choice!")
            I_understand = None
            I_understand = input("Enter anything to continue")
            if I_understand != None:
                Manage_employees.display_menu()

        if choice == 1:
            Manage_employees.display_menu()

        if choice == 2:
            Manage_properties.display_menu()

        if choice == 3:
            pass
            #Manage_maintenance_reports.display_menu()

        if choice == 4:
            pass
            #Manage_contractors.display_menu()
    
        if choice == 5:
            Manage_Locations.display_Locations()
        
        if choice == 0:
            Mainmenu_ui.display_menu()


import os
from ui.main_ui import Mainmenu_ui
from ui.manage_employee_ui import Manage_employees
#from ui.manage_properties_ui import Manage_properties
from ui.manage_locations_ui import Manage_Locations