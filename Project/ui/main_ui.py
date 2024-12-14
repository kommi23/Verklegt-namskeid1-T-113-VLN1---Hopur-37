
from logic.logic_wrapper import LogicWrapper
from ui.manage_locations_ui import Manage_Locations
from ui.manage_properties_ui import Manage_properties
from ui.manage_employee_ui import Manage_employees
from ui.maintenance_ui import Maintenance_ui
from ui.common_functions_ui import Common_functions
from ui.manager_ui import Manager_ui
from ui.employee_ui import Employee_ui


class Mainmenu_ui:
    def __init__(self):
        self.llw = LogicWrapper()
        self.comon = Common_functions(self.llw)
        self.man_loc = Manage_Locations(self.llw)
        self.man_pro = Manage_properties(self.llw)
        self.man_emp = Manage_employees(self.llw, self.comon)
        self.manmain = Maintenance_ui(self.llw, self.comon)
        self.eui = Employee_ui(self.llw, self.comon, self.manmain)
        self.mui = Manager_ui(self.llw, self.man_loc, self.man_emp, self.man_pro, self.manmain, self.man_loc)
         

    def display_menu(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Employee")
            print("2. Manager")
            print("0. Exit")

        
            choice = ""
            choice = str(input("Enter your choice: "))
            valid_choices = ["1","2","0"]

            if choice not in valid_choices:
                print("Please enter a valid choice!")
                I_understand = None
                I_understand = input("Enter anything to continue")
                if I_understand != None:
                    continue

            if choice == '1':
                self.eui.display_menu()

            elif choice == '2':
                self.mui.display_menu()
            
            elif choice == '0':
                quit()


