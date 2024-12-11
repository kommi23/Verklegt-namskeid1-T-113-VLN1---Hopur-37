from ui.manage_employee_ui import *

class SearchEmployeeEmpUI:
    def emp_search_menu():


        print("#########################")
        print("     Employee search     ")
        print("#########################")
        print("1. View all employees")
        print("2. search by name")
        print("3. seach by id")
        print("4. search by location")
        print("5. return")
        choice = int(input("Enter your choice: "))
        try:
            if choice == 1:
                Manage_employees.display_employees()
            if choice == 2:
                Manage_employees.search_employee_by_name()
            if choice == 3:
                Manage_employees.search_employee_by_id()
            if choice == 4:
                Manage_employees.search_employee_by_location()
            if choice == 5:
                Manage_employees.display_menu()
            else:
                print("Invalid input. Please enter choices 1-5: ")
        except RuntimeError:
            print("bara profa")