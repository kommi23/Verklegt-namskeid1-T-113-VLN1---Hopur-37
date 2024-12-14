from data.employee_data import EmployeeData 
from data.property_data import PropertyData
from data.location_data import LocationData
from data.maintenancerequests_data import MaintenanceRequestData

class DataLayerWrapper():
    def __init__(self):
        self.demp = EmployeeData()
        self.dpro = PropertyData()
        self.dloc = LocationData()
        self.dman = MaintenanceRequestData()

    # employee 
    def write_employee_dw(self,employee): 
        return self.demp.write_employe_data(employee) 
        

    def get_singular_employee_dw(self,employee_id):
        return self.demp.get_singular_employee_data(employee_id)

    def get_employees_dw(self) -> list:    
        return self.demp.get_employees_data()

    def get_employees_location_dw(self,location):
        return self.demp.get_employees_location_data(location)

    def delete_employee_dw(self,employee_id):
        x = self.demp.delete_employee_data(employee_id)
        if x == True:
            print("success")
        else: print(":(")

    def update_employee_dw(self,employee_id,updated_data, what_data):
        return self.demp.update_employee_data(employee_id, updated_data, what_data)

    # properies 
    def get_all_properties_dw(self,):
        return self.dpro.get_all_proberties_data()
    
    def get_property_by_number_dw(self,number):
        return self.dpro.get_singular_property_data(number)
    
    def get_property_by_location_dw(self,location):
        return self.dpro.get_properties_by_location_data(location)
    
    def add_property_dw(self,property):
        return self.dpro.add_property_data(property)
    
    def delete_property_dw(self,property_number):
        return self.dpro.delete_property_data(property_number)
    
    def update_property_dw(self,id, info_change, what_info):
        return self.dpro.update_property_data(id, info_change, what_info)

    # location 
    def update_location_data(self,property_number, updated_data, what_data): 
        return self.dloc.update_location_data(property_number, updated_data, what_data)
    
    def get_all_locations(self):
        return self.dloc.get_locations_data()

    # requests
    def add_maintenance_request_dw(self,new_request):
        return self.dman.add_maintenance(new_request)
        
    def get_all_maintenance_requests_dw(self):
        return self.dman.get_maintenances()
    
    def get_maintenance_request_by_id_dw(self,maintenance_id):
        return self.dman.get_maintenancerequest_by_ID(maintenance_id)
    
    def get_maintenance_request_by_property_id_dw(self,property_id):
        return self.dman.get_maintenancereports_by_property(property_id)
    
    def get_maintenance_request_by_employee_id_dw(self,employee_id):
        return self.dman.get_maintenancerequest_by_employee(employee_id)

    def update_maintenance_request_dw(self,maintenance_id, updated_data, what_data):
        return self.dman.update_maintenancerequest_data(maintenance_id, updated_data, what_data)
    
    def add_maintenance_report_dw(self,maintenance_id, employee_id, report):
        return self.dman.add_maintenancereport_data(maintenance_id, employee_id, report)
    
    def add_approve_maintenance_report_dw(self,maintenance_id):
        return self.dman.approve_maintenancereport_data(maintenance_id)

