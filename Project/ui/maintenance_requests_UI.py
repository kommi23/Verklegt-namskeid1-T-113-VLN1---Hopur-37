class MaintenanceReuquestsUI:
    def display_menu():
        print("#########################")
        print("  Maintenance Requests  " )
        print("#########################")
        print("1. view maintenance requests")
        print("2. search maintenance requests")
        print("3. Return")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                pass
            if choice == 2:
                pass
            if choice == 3:
                Employee_ui.display_menu()
                
            else:
                print("Invalid input")
        
        except ValueError:
            print("Please enter an integer between 1 - 3: ")

    

from ui.employee_ui import *
