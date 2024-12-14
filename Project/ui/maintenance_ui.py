
from ui.common_functions_ui import Common_functions
from logic.logic_wrapper import LogicWrapper
from Models.Maintenance_request import Maintenance_request

class Maintenance_ui:
    def __init__(self, llw: LogicWrapper, common : Common_functions):
        self.llw = llw
        self.common = common


    def manager_maintenance_requests_menu(self):
        while True:
            print("\n==Maintenance Request/Report Menu==")
            print("1. Display all Maintenance/Report Requests")
            print("2. Add Maintenance Request")
            print("3. Update Maintenance Request")
            print("4. Search Maintenance Request/Report by ID")
            print("5. Search Maintenance Requests/Reports by Property Number")
            print("6. Search Maintenance Requests/Reports by employee ID")        
            print("7. Approve Maintenance report")
            print("0. Go back")

            choice = (input("Enter your choice: "))
            valid_choices = ["1", "2", "3", "4", "5", "6", "7", "0"]

            if choice not in valid_choices:
                print("Please enter a valid choice: ")
                continue
            elif choice == '1':
                self.common.display_all_maintenace_requests()                
            elif choice == '2':
                self.add_maintenance_requests()
            elif choice == '3':
                self.update_maintenance_requests()
            elif choice == '4':
                self.common.search_maintenace_request_by_id()
            elif choice == '5':
                self.common.search_maintenances_request_by_property_id()
            elif choice == '6':
                self.common.search_maintenances_requests_by_employee_id()
            elif choice == "7":
                self.manager_approve_maintenance_report()
            elif choice == '0':
                return
             
            
    def add_maintenance_requests(self):
        print("\n=== Add New Maintenance Request ===")
        fields = ["Id","Property Number","Description","Priority","Date","Budget","Recurring Task"]
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
                self.llw.add_maintenance_request_lw(new_maintenance)
                print("\nMaintenance request added successfully!")
        else:
            print("Something went worng")    

            
    def update_maintenance_requests(self):
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
            print("Information not found")
            return
        else:
            print("You have entered the following details:")
            print(f"ID: {id}")
            print(f"{info_change}: {new_info}")

        smu = input("Press '1' to confirm the the information is correct: ")
        if smu == "1":
            try:
                self.llw.update_maintenance_request_lw(maintenance_id, new_info, info_list[info_change])
                input(f"Maintenance Request {info_change} updated successfully, press any key to continue")
            except RuntimeError as re:
                print(re)
        return

    def employee_write_maintenance_report(self):
        maintenance_id = input("Enter Maintenance Number: ")
        employee_id = input("Enter your id: ")
        report = input(f"Write a report for request {maintenance_id}: ")
        try: 
            self.llw.add_maintenance_report_lw(maintenance_id, employee_id, report)
            input(f"Success, press any key to continue")
        except RuntimeError as re:
            print(re)
        return


    def manager_approve_maintenance_report(self):
        maintenance_id = input("Enter Maintenance Number: ")

        print(f"1. To approve maintenance report {maintenance_id}")
        print("0. To go back")
        choice = input("Enter your choice: ")
        valid_choices = ["1", "0"]

        if choice not in valid_choices:
            print("Please enter a valid choice: ")
            return self.manager_approve_maintenance_report()
    
        if choice == '1':
            try:
                self.llw.approve_maintenance_report_lw(maintenance_id)
            except:
                return
            
        elif choice == '0':
            return 