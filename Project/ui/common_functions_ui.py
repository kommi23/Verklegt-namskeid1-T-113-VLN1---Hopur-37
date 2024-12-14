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
            return LL_employee.search_employee_id_lw(id)
            

    def search_employee_by_location():
        location = input("Enter Employee Location to search from: ")
        employees = LL_employee.search_employee_location_lw(location)

    # Vantar að setja í logic wrapperinn
    def display_all_maintenace_requests():
        requests = []
        requests = LW_maintenance_request.get_all_maintenance_requests_lw()

        if not requests:
            print("No Maintenance Requests/Reports found...")

        else:
             for i in requests:
                  print(i)
    
    

    def search_maintenace_request_by_id():
        id = (input("Enter the ID for the Maintenance Request/Report:"))


        request = LW_maintenance_request.get_maintenance_request_by_id_lw(id)

        #request = LW_maintenance_request.get_maintenance_request_by_employee_id_lw(id)

        
        if not request:
            print(f"No Maintenance Request/Report found with the ID {id}")

        else:
            print(request)
    
    def search_maintenances_request_by_property_id():
        property_number = input("Enter the Property ID for the Maintenance Requests/Reports: ")
        requests = LW_maintenance_request.get_maintenance_request_by_property_id_lw(property_number)

        if not requests:
              print("No Maintenance Request/Report found with Propery Number {property_id}")

        else:
            for request in requests:
                print(request)

    def search_maintenances_requests_by_employee_id():
        employee_id = input("Enter the Employee ID for the Maintenance Requests/Reports: ")
        requests = LW_maintenance_request.get_maintenance_request_by_property_id_lw(employee_id)

        if not requests:
              print("No Maintenance Request/Report found with Propery Number {property_id}")

        else:
            for request in requests:
                print(request)      