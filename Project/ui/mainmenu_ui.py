from ui.employee_ui import EmployeeMenuUI

class Mainmenu_UI:
     def __init__(self, employee, manager, contractor):
        self.employee = employee
        pass
          
def display_menu(self):
        # forsiða
        while True:
            print("\nMain Menu")
            print("1. Employee")
            print("2. Manager")
            print("3. Contractor")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.employee_menu()
            elif choice == '2':
                self.manager_menu()
            elif choice == '3':
                self.contractor_menu()
            elif choice == '4':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")