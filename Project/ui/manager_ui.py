class Manager_ui:
    def display_menu():
        print("1. Manage Employees")
        print("2. Manage Properties")
        print("3. Manage maintainance requests")
        print("4. Show all locations")
        #print("5. Manage Contractors")
        print("0. Go back")
        choice = input("Enter your choice:")

        if choice == 1:
            Manage_employees.display_menu()
            Manager_ui.display_menu()

        if choice == 2:
            Manage_properties.display_menu()
            Manager_ui.display_menu()

        if choice == 3:
            Maintenance_ui.manager_maintenance_requests_menu()
    
        if choice == 4:
            Manage_Locations.display_Locations()
            Manager_ui.display_menu()

        #if choice == "5":
        #    pass
        #    Manage_contractors.display_menu()
        
        if choice == 0:
            Mainmenu_ui.display_menu()
        
        else:
            print("Please select a choice between 0-4")
            Manager_ui.display_menu()



from ui.maintenance_ui import Maintenance_ui
from ui.main_ui import Mainmenu_ui
from ui.manage_employee_ui import Manage_employees
from ui.manage_properties_ui import Manage_properties
from ui.manage_locations_ui import Manage_Locations