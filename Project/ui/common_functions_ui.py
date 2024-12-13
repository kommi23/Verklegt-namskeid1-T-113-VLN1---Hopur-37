from logic.logic_wrapper import *
from Models.Maintenance_request import *
class Common_functions:

    def display_employees():
        list_of_employees = []
        list_of_employees = LL_employee.get_employee_list_lw()
                
        if not list_of_employees:
                print("No employees found.")

        else:
            for employee in list_of_employees:
                    print(employee)

    def search_employee_by_id(): #virkar
            id = input("Enter Employee ID to search: ")
            employee1 = LL_employee.search_employee_id_lw(id)
            return employee1

    def search_employee_by_location():
        location = input("Enter Employee Location to search from: ")
        employees = LL_employee.search_employee_location(location)
        if not employees:
            print("No employees found in location {location}.")
        
        else:
            for i in employees:
                print(i)
    
    # Vantar að setja í logic wrapperinn
    def display_maintenace_requests():
        requests = []
        requests = LL_Maintenance.list_all_maintenance_requests()

        if not requests:
            print("No Maintenance Requests found...")

        else:
             for i in requests:
                  print(i)
    
    def search_maintenace_request_by_id():
        id = (input("Enter the ID for the Maintenance Request:"))
        request = LL_Maintenance.search_maintenance_id(id)
        
        if not request:
             print("No Maintenance Request found with the ID {id}")

        else:
             request = Maintenance_request.turn_maintenance_request_into_list(request) 
             print(request)
