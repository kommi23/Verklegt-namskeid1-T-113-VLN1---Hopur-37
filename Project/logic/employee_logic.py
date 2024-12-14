from Models.Employee import *
from data.data_wrapper import DataLayerWrapper

class Employee_logic:
    def __init__(self, datalayerwrapper : DataLayerWrapper):
        self.dlw : DataLayerWrapper = datalayerwrapper

    def write_employee_logic(self, employee: list):
        # Get a list of all employees from the data layer
        all_employees = self.dlw.get_employees_dw()
        # Loop through all the employees and check if the id, name or email already exist in the db
        for existing_employee in all_employees:
            if employee.employee_id == existing_employee.employee_id:
                raise RuntimeError("An employee with this id already exists")
            
        # If none of the flags are raised return the employee for the data layer to append
        self.dlw.write_employee_dw(employee)

    #search employee by id
    def get_singular_employee_logic(self, id: int):
        employee1 = self.dlw.get_singular_employee_dw(id)
        if not employee1:
            return f"No employee found with the ID {id}."
        
        else:
            return employee1
    
    def get_employees_location_logic(self,location: str):
        try:
            return self.dlw.get_employees_location_dw(location) 
        except: 
            return f"No employees form location {location} found"

    def get_employee_list(self):
        return self.dlw.get_employees_dw()
    
    # Get the list of all employees in the data layer and send it to the UI layer
    def get_employees_logic(self):
        return self.dlw.get_employees_dw()
    



    # ON HOLD FOR NOW
    # Get employee from data layer and update it
    

    def delete_employee_logic(self, id):
        if self.dlw.delete_employee_dw():
            return f"Employee with id: {id} deleted"
        else:
            return f"Employee with id: {id} not found!"


    def update_employee_logic(self, id , updated_data, what_data: int):
        employee_change = self.dlw.update_employee_dw(id,updated_data, what_data)

        if employee_change:
            return f"Employee with ID {id} updated successfully."
        else:
            return f"Employee with ID {id} not found."


