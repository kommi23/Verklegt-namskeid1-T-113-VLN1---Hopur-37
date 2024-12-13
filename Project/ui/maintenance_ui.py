
from ui.common_functions_ui import *
from logic.logic_wrapper import *
from Models.Maintenance_request import *
from ui.manager_ui import *


class Maintenance_ui:
    def manager_maintenance_requests_menu():

        print("1. Display all Maintenance Requests")
        print("2. Add Maintenance Request")
        print("3. Update Maintenance Request")
        print("4. Search Maintenance Request by ID")
        print("5. Search Maintenance Request by Property Number")
        print("0. Go back")

        choice = (input("Enter your choice: "))
        valid_choices = ["1", "2", "3", "4", "5", "0"]

        if choice not in valid_choices:
            print("Please enter a valid choice: ")
            return
        elif choice == '1':
            Common_functions.display_all_maintenace_requests()
        elif choice == '2':
            add_maintenance_requests()
        elif choice == '3':
            update_maintenance_requests()
        elif choice == '4':
            Common_functions.search_maintenace_request_by_id()
        
        elif choice == '5':
            Common_functions.search_maintenance_request_by_property_id()
             
        elif choice == '0':
            Manager_ui.display_menu()
             




            
def add_maintenance_requests():
    print("\n=== Add New Maintenance Request ===")
    fields = ["Id","Property Number","Description","Priority","Date","Budget","Recurring Task","Employee ID"]
    user_input = {}

    
    for field in fields:
        user_input[field] = input(f"Enter Maintenance Request {field}: ")

    
    print("\nYou have entered the following details:")
    for key, value in user_input.items():
        print(f"{key}: {value}")

    
    confirmation = input("\nPress 1 to confirm or any other key to cancel: ")

    if confirmation == "1":
        
            new_maintenance = Maintenance_request(
                user_input["Id"],
                user_input["Property Number"],
                user_input["Description"],
                user_input["Priority"],
                user_input["Date"],
                user_input["Budget"],
                user_input["Recurring Task"],
            )

            Maintenance_request_logic.add_maintenance_request_logic(new_maintenance)
            print("\nMaintenance request added successfully!")
    else:
         print("Something went worng")    



            
def update_maintenance_requests():
        maintenance_id = input("Enter Maintenance Number: ")
        info_change = input("Enter what information to change (e.g, Property Number, Date): ").lower()
        new_info = input("Enter new information: ")

        info_list = { 
            
            "id": 1, 
            "property": 2,
            "description": 3,
            "priority": 4,
            "date": 5,
            "recurrin_task": 6,
        }


        if info_change not in info_list:
            print(f"Error: Information not found")
            
        
            
            LW_maintenance_request.update_maintenance_request_lw(maintenance_id, new_info, info_list[info_change])
            print(f"Maintenance Request {info_change} updated successfully")

def employee_write_maintenance_report():
    maintenance_id = input("Enter Maintenance Number: ")

    employee_id = input("Enter your id: ")

    report = input(f"Write a report for request {maintenance_id}: ")

    LW_maintenance_request.add_maintenance_report_lw(maintenance_id, employee_id, report)