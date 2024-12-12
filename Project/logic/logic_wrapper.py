from Models.Maintenance_request import *
from Models.Employee import *
from Models.Property import *

from logic.employee_logic import *
from logic.contractor_logic import *
from logic.property_logic import *
from logic.maintenance_request_logic import *
from logic.location_logic import Location_logic


class LL_employee():
    def add_employee_lw(new_employee) -> str:
        return Employee_logic.write_employee_logic(new_employee)
    

    def get_employee_list_lw() -> list:

        return Employee_logic.get_employee_list()
    
    def update_employee_lw(id: int, updated_data, what_data: int):
        return Employee_logic.update_employee_logic(id, updated_data, what_data)
    
    def search_employee_name_lw(name: str):
        return Employee.search_employee_name(name)
    
    def search_employee_id_lw(id: int) -> Employee:
        return Employee_logic.get_singular_employee_logic(id)
    
    def search_employee_location_lw(location: str) -> list:
        return Employee_logic.get_employees_location_logic(location)
    

class LL_contractor:
    def get_contractor_list_lw() -> list:
        return Contractor.get_contractor_list()
    
    def add_contractor_lw(contractor):
        Contractor.add_contractor(contractor)

    def update_contractor_lw(id: int, updated_data, what_data: int):
        Contractor.update_contractor(id, updated_data, what_data)

    def add_contractor_review_lw(id: int, review: str):
        Contractor.add_contractor_review(id, review)

    def get_contractor_review_lw(id) -> list :
        return Contractor.get_contractor_review
    
    def search_contractor_history_lw(id) -> list:
        return Contractor.search_contractor_maintainance_history(id)
        

class LL_property():
    def add_property_lw(property):
        Property_logic.add_property(property)
    
    def get_all_properties_lw() -> list:
        return Property_logic.get_all_proberties_logic()
     
    def get_properties_by_location_data_LL(location):
         return Property_logic.get_properties_by_location_data_logic(location)
        
    def change_property_lw(id, info_change, what_info) -> list:
        Property_logic.change_property(id, info_change, what_info)
        
class LL_location():

    def list_all_locations() -> list:
        return Location_logic.get_location_list()
        
class LW_maintenance_request:
    def add_maintenance_request_lw(new_request):
        return Maintenance_request_logic.add_maintenance_request_logic(new_request)
    
    def get_all_maintenance_requests_lw() -> list:
        return Maintenance_request_logic.get_all_maintenance_requests_logic()
    
    def get_maintenance_request_by_id_lw(maintenance_id: int):
        return Maintenance_request_logic.get_maintenance_request_by_id_logic(maintenance_id)
    
    def get_maintenance_request_by_property_id_lw(property_id: int):
        return Maintenance_request_logic.get_maintenance_request_by_property_id_logic(property_id)
    
    def get_maintenance_request_by_employee_id_lw(employee_id: int):
        return Maintenance_request_logic.get_maintenance_request_by_employee_id_logic(employee_id)

    

