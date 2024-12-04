class Employee:
    def __init__(self, id: int, name: str, location: str, phone_number: int, email: str, address: str):
        self.id = id
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def add_employee(self, data_wrapper, employee_list: list, employee: list):
        # Get a list of all employees from the data layer
        all_employees = data_wrapper.list_all_employees()
        # Loop through all the employees and check if the id, name or email already exist in the db
        for existing_employee in all_employees:
            if employee[0] == existing_employee[0]:
                return "An employee with this id already exists"
            if employee[1] == existing_employee[1]:
                return "An employee with this name already exists"
            if employee[4] == existing_employee[4]:
                return "An employee with this email already exists"
            
        # If none of the flags are raised append the new employee to the employee list and return it
        employee_list.append(employee)
        return employee_list

    # Get the list of all employees in the data layer and send it to the UI layer
    def get_employee_list(data_wrapper, __):

        return data_wrapper.list_all_employees()

    # Get employee from data layer and update it
    def update_employee(data_wrapper, id: int, updated_data: dict):
        employee = data_wrapper.search_employee_id(id)

        if employee:
            data_wrapper.update_employee_data(id, updated_data)
            return f"Employee with ID {id} updated successfully."
        else:
            return f"Employee with ID {id} not found."

    def search_employee_name(data_wrapper, name: str):
        all_employees = data_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[1] == name:
                return existing_employee

        return f"Employee with name {name} not found"

    def search_employee_id(data_wrapper, id: int):
        all_employees = data_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[0] == id:
                return existing_employee

        return f"Employee with ID {id} not found"

    def search_employee_location(data_wrapper, location: str):
        all_employees = data_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[2] == location:
                return existing_employee

        return f"No employees form location {location} found"
