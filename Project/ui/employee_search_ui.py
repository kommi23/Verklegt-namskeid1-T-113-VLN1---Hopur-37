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
        print("0. return")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            Manage_employees.display_employees()
            Manage_employees.display_menu()
        if choice == 2:
            Manage_employees.search_employee_by_name()
            Manage_employees.display_menu()
        if choice == 3:
            Manage_employees.search_employee_by_id()
            Manage_employees.display_menu()
        if choice == 4:
            Manage_employees.search_employee_by_location()
            Manage_employees.display_menu()
        if choice == 0:
            Manage_employees.display_menu()
        else:
            print("Invalid input. Please enter choices 1-5: ")
            Manage_employees.display_menu()
