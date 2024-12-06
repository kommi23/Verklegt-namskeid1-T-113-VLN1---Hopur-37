from logic_layer import Employee

class EmployeeMenu_UI:
    def __init__(self):
        self.employee_logic = employee_logic

    def employee_menu(self):
        print("Employee Menu")
        print("1. Add employee")
        print("2. search for employee")
        print("3. change employee")
        print("E. Go back")
    
    def input_menu(self):
        while True:
            self.output_menu()
            user_input = input("Enter your choice: ")
            user_input = user_input.lower()
            if user_input == "1":
                emp = employee()
                emp.name = input("Enter employee's name: ")
                emp.ID = input("Enter employee's ID: ")
                emp.email = input("Enter employee's email: ")
                emp.address = input("Enter employee's address: ")
                emp.work_phone = input("Enter employee's work phone: ")
                emp.personal_phone = input("Enter employee's personal phone: ")
                emp.location = input("Enter employee's location: ")
                self.employee_logic.create.employee(e)

