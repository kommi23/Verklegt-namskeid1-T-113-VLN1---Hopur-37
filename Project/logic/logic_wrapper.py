class LL_employee():
    def add_employee(new_employee) -> str:
        return Employee_logic.write_employee_logic(new_employee)
    

    def get_employee_list() -> list:
        return Employee_logic.get_employee_list
    

    def update_employee(id: int, updated_data, what_data: int) -> str:
        return Employee_logic.update_employee_logic(id, updated_data, what_data)
    
    def search_employee_name(name: str) -> list:
        return Employee.search_employee_name(name)
    
    def search_employee_id(id: int) -> list:
        return Employee_logic.get_singular_employee_logic(id)
    
    def search_employee_location(location: str) -> list:
        return Employee_logic.get_employees_location_logic(location)
    
class LL_contractor:
    def get_contractor_list() -> list:
        return Contractor.get_contractor_list()
    
    def add_contractor(contractor: list):
        Contractor.add_contractor(contractor)

    def update_contractor(id: int, updated_data, what_data: int):
        Contractor.update_contractor(id, updated_data, what_data)

    def add_contractor_review(id: int, review: str):
        Contractor.add_contractor_review(id, review)

    def get_contractor_review(id) -> list :
        return Contractor.get_contractor_review
    
    def search_contractor_history(id) -> list:
        return Contractor.search_contractor_maintainance_history(id)
        
class LL_property():
     
    def add_property(property):
        Property_logic.add_property(property)
    
    def get_all_proberties_LL():
        return Property_logic.get_all_proberties_logic()
        
    def change_property_lw(id, info_change, what_info):
        Property_logic.change_property(id, info_change, what_info)
        
        

    
    
from logic.employee_logic import *
from logic.contractor_logic import *
from logic.property_logic import *
from Models.Employee import *