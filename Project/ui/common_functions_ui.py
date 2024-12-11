from logic.logic_wrapper import *

class Common_functions:

    def display_employees():
        employees = []
        employees = LL_employee.list_all_employees()
                
        if not employees:
                print("No employees found.")

        else:
            for i in employees:
                    print(i)

    def search_employee_by_id(): #virkar
            id = input("Enter Employee ID to search: ")
            employee = LL_employee.search_employee_id(id)
            if not employee:
                print("No employee found with the ID {id}.")
            
            else:
                employee = Employee.turn_employee_into_list(employee)
                #print(tabulate(table, headers=["ID", "Name", "Location", "Phone Number", "Email", "Address"], tablefmt="grid"))
                print(employee)

    def search_employee_by_location():
        location = input("Enter Employee Location to search from: ")
        employees = LL_employee.search_employee_location(location)
        if not employees:
            print("No employees found in location {location}.")
        
        else:
            for i in employees:
                print(i)