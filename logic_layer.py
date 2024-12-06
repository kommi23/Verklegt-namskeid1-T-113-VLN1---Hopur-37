class Employee:
    def __init__(self, id: int, name: str, location: str, phone_number: int, email: str, address: str):
        self.id = id
        self.name = name
        self.location = location
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self) -> str:
        return f"[{self.id}, {self.name}, {self.location}, {self.phone_number}, {self.email}, {self.address}]"

    def add_employee(employee: list):
        # Get a list of all employees from the data layer
        all_employees = dl_wrapper.list_all_employees()
        # Loop through all the employees and check if the id, name or email already exist in the db
        for existing_employee in all_employees:
            if employee.id == existing_employee.id:
                raise RuntimeError("An employee with this id already exists")
            elif employee.name == existing_employee.name:
                raise RuntimeError("An employee with this name already exists")
            elif employee.email == existing_employee.email:
                raise RuntimeError("An employee with this email already exists")
            else:
                # If none of the flags are raised return the employee for the data layer to append
                return employee 

    # Get the list of all employees in the data layer and send it to the UI layer
    def get_employee_list():

        return dl_wrapper.list_all_employees()

    # Get employee from data layer and update it
    def update_employee(self, id: int, updated_data, what_data: int):
        employee = dl_wrapper.search_employee_id(id)

        if employee[0] == id:
            employee[what_data] = updated_data
            dl_wrapper.update_employee(employee)
            return f"Employee with ID {id} updated successfully."
        else:
            return f"Employee with ID {id} not found."

    def search_employee_name(self, name: str):
        all_employees = dl_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[1] == name:
                return existing_employee

        return f"Employee with name {name} not found"

    def search_employee_id(self, id: int):
        all_employees = dl_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[0] == id:
                return existing_employee

        return f"Employee with ID {id} not found"

    def search_employee_location(self, location: str):
        all_employees = dl_wrapper.list_all_employees()
        for existing_employee in all_employees:
            if existing_employee[2] == location:
                return existing_employee

        return f"No employees form location {location} found"


class Contractor:

    def __init__(self, id: int, name: str, location: str, gsm: int, address: str, opening_hours: str):
        self.id = id
        self.name = name
        self.location = location
        self.gsm = gsm
        self.address = address
        self.opening_hours = opening_hours

    def get_contractor_list(self, ):
        return dl_wrapper.get_contractor_list()

    def add_contractor(self, contractor: list):
        # Get list of all the contractors
        list_of_contractors = dl_wrapper.get_contractor_list()

        # Check if the id or the name already exists in the db, if so raise a runtime error
        for existing_contractor in list_of_contractors:
            if contractor[0] == existing_contractor[0]:
                raise RuntimeError("A contractor with this ID already exists")
            elif contractor[1] == existing_contractor[1]:
                raise RuntimeError("A contractor with this name already exists")
            
            # If no error is raised return the contractor and send to data_layer
            else:
                return contractor

    def update_contractor(self, id: int, updated_data, what_data: int):
        # On hold for testing
        """
        contractor_list = data_wrapper.get_contractor_list()

        for contractor in contractor_list:
            if id == contractor[0]:
        """
        pass


    def get_contracotor_review(self):
        pass

    def add_contractor_review(self):
        pass

    def get_contractor_review(self):
        pass

    def search_contractor_by_name(self):
        pass
    
    def search_contractor_by_gsm(self):
        pass

    def search_contractor_by_location(self):
        pass

    def search_contractor_maintainance_history(self):
        pass






######### TEST CASE #########
class dl_wrapper:
    def list_all_employees():
        return test_all_employees

employee_a = Employee(1, "Alex", "Reykjavik", 6151306, "alexanderje24@ru.is", "Heima 1")
employee_b = Employee(2, "John", "Malmo", 5812345, "jon@mamlo.net", "Heima 2")
new_employee = Employee(3, "Doe", "Berlin", 5885522, "doe@berlin.de", "Heima 3")

test_all_employees = [employee_a, employee_b]
    
new_list = Employee.get_employee_list()

for employee in new_list:
    print(employee)


#from data_wrapper import * 