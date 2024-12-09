class Employee:
    def __init__(self, id: int, name: str, location: str, phone_number: int, email: str, address: str):
        
        self.id = id
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.email = email
        self.address = address


    def turn_into_list(id: int, name: str, location: str, phone_number: int, email: str, address: str):
        employee = []
        employee.append(id)
        employee.append(name)
        employee.append(location)
        employee.append(phone_number)
        employee.append(email)
        employee.append(address)
        print("DEBUG STRING|| After turn_into_list")
        print(employee)
        return employee

    def __str__(self) -> str:
        return f"[{self.id}, {self.name}, {self.location}, {self.phone_number}, {self.email}, {self.address}]"

    def write_employee_logic(employee: list):
        # Get a list of all employees from the data layer
        all_employees = dw_employee.get_employees_dw()
        # Loop through all the employees and check if the id, name or email already exist in the db
        for existing_employee in all_employees:
            if employee[0] == existing_employee[0]:
                raise RuntimeError("An employee with this id already exists")
            
        # If none of the flags are raised return the employee for the data layer to append
        dw_employee.write_employee_dw(employee)

    #search employee by id
    def get_singular_employee_logic(id: int):
        dw_employee.get_singular_employee_dw(id)

    
    # Get the list of all employees in the data layer and send it to the UI layer
    def get_employees_logic():
        return dw_employee.get_employees_dw()
    

    def get_employees_location_logic(location: str):
        try:
            return dw_employee.get_employees_location_dw(location) 
        except: 
            return f"No employees form location {location} found"

    # ON HOLD FOR NOW
    # Get employee from data layer and update it
    

    def delete_employee_logic(id):
        if dw_employee.delete_employee_dw(employee_id):
            return f"Employee with id: {id} deleted"
        else:
            return f"Employee with id: {id} not found!"


    def update_employee_logic(id: int, updated_data, what_data: int):
        employee_change = dw_employee. update_employee_dw(id,updated_data, what_data)

        if employee_change:
            return f"Employee with ID {id} updated successfully."
        else:
            return f"Employee with ID {id} not found."


from data.data_wrapper import *