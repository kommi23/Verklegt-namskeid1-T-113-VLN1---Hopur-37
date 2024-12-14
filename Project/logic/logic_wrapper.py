from Models.Maintenance_request import Maintenance_request
from Models.Employee import Employee
from Models.Property import Property

from logic.employee_logic import Employee_logic
from logic.property_logic import Property_logic
from logic.maintenance_request_logic import Maintenance_request_logic
from logic.location_logic import Location_logic
from data.data_wrapper import DataLayerWrapper

class LogicWrapper():
    def __init__(self):
        self.dlw = DataLayerWrapper()
        self.lemp = Employee_logic(self.dlw)
        self.lpro = Property_logic(self.dlw)
        self.lloc = Location_logic(self.dlw)
        self.matn = Maintenance_request_logic(self.dlw)

    # employees 
    def add_employee_lw(self, new_employee) -> str:
        return self.lemp.write_employee_logic(new_employee)
    
    def get_employee_list_lw(self) -> list:
        return self.lemp.get_employee_list()
    
    def update_employee_lw(self, id: int, updated_data, what_data: int):
        return self.lemp.update_employee_logic(id, updated_data, what_data)
    
    def search_employee_id_lw(self, id: int) -> Employee:
        return self.lemp.get_singular_employee_logic(id)
    
    def search_employee_location_lw(self, location: str) -> list:
        return self.lemp.get_employees_location_logic(location)

    # properties 
    def add_property_lw(self, property):
        return self.lpro.add_property(property)
    
    def get_all_properties_lw(self) -> list:
        return self.lpro.get_all_proberties_logic()

     
    def get_properties_by_location_data_LL(self, location):
         return self.lpro.get_properties_by_location_data_logic(location)

    def change_property_lw(self, id, info_change, what_info) -> list:
        return self.lpro.change_property(id, info_change, what_info)
    
    
    # location 

    def list_all_locations(self) -> list:
        return self.lloc.get_location_list()
        
    # maintenance_request:
    def add_maintenance_request_lw(self, new_request):
        return self.matn.add_maintenance_request_logic(new_request)
    
    def get_all_maintenance_requests_lw(self) -> list:
        return self.matn.get_all_maintenance_requests_logic()
    
    def get_maintenance_request_by_id_lw(self,maintenance_id: int):
        return self.matn.get_maintenance_request_by_id_logic(maintenance_id)
    
    def get_maintenance_request_by_property_id_lw(self,property_id: int):
        return self.matn.get_maintenancerequest_by_property_id(property_id)
    
    def get_maintenance_request_by_employee_id_lw(self,employee_id: int):
        return self.matn.get_maintenancereports_by_employee(employee_id)
    
    def update_maintenance_request_lw(self,maintenance_id: int, updated_data, what_data: int):
        return self.matn.update_maintenance_logic(maintenance_id, updated_data, what_data)
    
    def add_maintenance_report_lw(self,maintenance_id: int, employee_id, report):
        return self.matn.add_maintenance_report_logic(maintenance_id, employee_id, report)
    
    def approve_maintenance_report_lw(self,maintenance_id: int):
        return self.matn.approve_maintenace_report_logic(maintenance_id)
    
