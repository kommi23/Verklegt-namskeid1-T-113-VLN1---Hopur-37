from ui.maintenance_ui import Maintenance_ui
from ui.manage_employee_ui import Manage_employees
from ui.manage_properties_ui import Manage_properties
from ui.manage_locations_ui import Manage_Locations
from ui.common_functions_ui import Common_functions
from logic.logic_wrapper import LogicWrapper

class Manager_ui:
    def __init__(self, llw : LogicWrapper, comon : Common_functions, manemp: Manage_employees, manprop : Manage_properties, manmain : Maintenance_ui, manloc : Manage_Locations):
        self.llw : LogicWrapper = llw
        self.comon = comon
        self.manemp = manemp
        self.manprop = manprop
        self.manmain = manmain
        self.manloc = manloc

    def display_menu(self):
        while True:
            print("\n=== Mananger Menu ===")
            print("1. Manage Employees")
            print("2. Manage Properties")
            print("3. Manage maintainance requests")
            print("4. Show all locations")
            print("0. Go back")

            choice = str(input("Enter your choice:"))
            #valid_choices = ["1", "2", "3", "4", "5", "0"]
            valid_choices = ["1", "2", "3", "4", "0"]
            
            if choice not in valid_choices:
                print("Please enter a valid choice!")
                I_understand = None
                I_understand = input("Enter anything to continue")
                if I_understand != None:
                    continue

            if choice == "1":
                self.manemp.display_menu()

            if choice == "2":
                self.manprop.display_menu()

            if choice == "3":
                self.manmain.manager_maintenance_requests_menu()
        
            if choice == "4":
                self.manloc.display_Locations()

            #if choice == "5":
            #    pass
            #    Manage_contractors.display_menu()
            
            if choice == "0":
                return


