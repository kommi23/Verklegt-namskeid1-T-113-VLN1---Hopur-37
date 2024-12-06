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

    def add_employee(employee: list):
        print("DEBUG PRINT|| in the beginning of add_employee")
        # Get a list of all employees from the data layer
        all_employees = dw_employee.get_employees()
        print("DEBUG PRINT|| After fetching the list")
        # Loop through all the employees and check if the id, name or email already exist in the db
        for existing_employee in all_employees:
            if employee[0] == existing_employee[0]:
                raise RuntimeError("An employee with this id already exists")
            if employee[1] == existing_employee[1]:
                raise RuntimeError("An employee with this name already exists")
            if employee[3] == existing_employee[3]:
                raise RuntimeError("An employee with this email already exists")
        
        # If none of the flags are raised return the employee for the data layer to append
        dw_employee.write_employee(employee)

    # Get the list of all employees in the data layer and send it to the UI layer
    def get_employee_list():

        return dw_employee.get_employees()


    # ON HOLD FOR NOW
    # Get employee from data layer and update it
    """
    def update_employee(self, id: int, updated_data, what_data: int):
        employee = dw_employee.search_employee_id(id)

        if employee[0] == id:
            employee[what_data] = updated_data
            dl_wrapper.update_employee(employee)
            return f"Employee with ID {id} updated successfully."
        else:
            return f"Employee with ID {id} not found."
    """        

    # On hold for now
    """
    def search_employee_name(self, name: str):
        all_employees = dl_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[1] == name:
                return existing_employee

        return f"Employee with name {name} not found"
    """

    def search_employee_id(self, id: int):
        dw_employee.get_employee(id)

        # Dont want to delete yet in case the other does not work
        """
        all_employees = dl_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[0] == id:
                return existing_employee

        return f"Employee with ID {id} not found"
        """

    def search_employee_location(self, location: str):
        pass
        """
        all_employees = dw_employee.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[2] == location:
                return existing_employee
        """

        return f"No employees form location {location} found"

from data.data_wrapper import *