
from logic.employee_logic import Employee
from logic.logic_wrapper import ll_employee
    
class EmployeeUI:
     
    def __init__(self):
        self.logic_wrapper = ll_employee()

    def employee_menu(self):
        print("Employee Menu")
        print("1. Add employee")
        print("2. list all employees")
        print("3. change employee")
        print("E. Go back")
    
    def input_menu(self):
        while True:
            self.employee_menu()
            user_input = input("Enter your choice: ")
            user_input = user_input.lower()
            if user_input == 'e':
                 print("Returning")
                 break

            elif user_input == '1':
                emp = Employee()
                emp.name = input("Enter employee's name: ")
                emp.ID = input("Enter employee's ID: ")
                emp.email = input("Enter employee's email: ")
                emp.address = input("Enter employee's address: ")
                emp.work_phone = input("Enter employee's work phone: ")
                emp.personal_phone = input("Enter employee's personal phone: ")
                emp.location = input("Enter employee's location: ")
                self.logic_wrapper.add_employee(emp)
            
            elif user_input == '2':
                results = self.logic_wrapper.get_employee_list()
                # ELements inside list
                for  elem in results:
                     print(f"name: {elem.name}, ID: {elem.ID}, email: {elem.email}, address: {elem.address}, work phone: {elem.work_phone}, personal phone: {elem.personal_phone}, location: {elem.location}")