import os
from logic.logic_wrapper import LogicWrapper
from ui.common_functions_ui import Common_functions
from ui.maintenance_ui import Maintenance_ui

class Employee_ui:

    def __init__(self, llw : LogicWrapper, comon : Common_functions, manmain : Maintenance_ui):
        self.llw : LogicWrapper = llw, 
        self.comon = comon
        self.manmain : Maintenance_ui = manmain

    def display_menu(self):
        while True:
            print("\n==Employee Menu==")
            print("1. List all employees")
            print("2. Search for employee")
            print("3. Available Maintenance Requests")
            print("4. Search for Maintenance Requests")
            print("5. Add Maintenance Report")
            print("0. Go back")

            choice = str(input("Enter your choice:"))

            if choice == "0":
                return 

            valid_choices = ["1", "2", "3", "4", "5", "0"]

            if choice not in valid_choices:
                print("Please enter a valid choice!")
                I_understand = None
                I_understand = input("Enter anything to continue")
                if I_understand != None:
                    continue
            
            
            
            if choice == "1":
                self.comon.display_employees()

            if choice == "2":
                # submenue .. 
                choice2 = ""
                while choice2 != "0":
                    print("\nDo you want to:")
                    print("1. Search for employee by ID ")
                    print("2. Search for employee by Location ")
                    print("0. Go back")

                    choice2 = str(input("Enter your choice:"))
                    valid_choices = ["1", "2", "0"]

                    if choice2 not in valid_choices:
                        print("Please enter a valid choice!")
                        I_understand = None
                        I_understand = input("Enter anything to continue")
                        if I_understand != None:
                            continue

                    if choice2 == "1":
                        employee1 = self.comon.search_employee_by_id()
                        print(employee1)

                    if choice2 == "2":
                        self.comon.search_employee_by_location()
                    
                    if choice2 == "0":
                        return
                # end while 2 

            if choice == "3":  
                self.comon.display_all_maintenace_requests()

            if choice == "4":
                self.comon.search_maintenace_request_by_id()

            if choice == "5":
                self.manmain.employee_write_maintenance_report()

            
                

 