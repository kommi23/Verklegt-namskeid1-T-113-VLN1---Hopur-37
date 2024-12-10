class employee_logic:

    def write_employee_logic(employee: list):
        # Get a list of all employees from the data layer
        all_employees = dw_employee.get_employees_dw()
        # Loop through all the employees and check if the id, name or email already exist in the db
        for existing_employee in all_employees:
            if employee.employee_id == existing_employee.employee_id:
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
        if dw_employee.delete_employee_dw():
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