from data.data_wrapper import DataLayerWrapper
from Models.Maintenance_request import *

class Maintenance_request_logic:

    def __init__(self, datawrapper: DataLayerWrapper):
        self.dwl = datawrapper

    def add_maintenance_request_logic(self, new_request):
        
        all_requests = self.dwl.get_all_maintenance_requests_dw()

        for request in all_requests[1:]:
            
            if request.id == new_request.id:
                raise RuntimeError(f"A maintenance request with the id {new_request.id} already exists")
        
        return self.dwl.add_maintenance_request_dw(new_request)
    
    def get_all_maintenance_requests_logic(self):
        return self.dwl.get_all_maintenance_requests_dw()
    
    def get_maintenance_request_by_id_logic(self, maintenance_id):
        return self.dwl.get_maintenance_request_by_id_dw(maintenance_id)

 
    def get_maintenancereports_by_employee(self, employee_id: int) -> list[Maintenance_request]:
        """Returns a list of all MaintenanceReports that the employee is registered to.
        """
        maintenencerequest = []
        all_maintenance_reports = self.dwl.get_all_maintenance_requests_dw()
        for maintenance_report in all_maintenance_reports:
            if maintenance_report.employee_id == employee_id:
                maintenencerequest.append(maintenance_report)
        return maintenencerequest
    

    
    def get_maintenancerequest_by_property_id(self, property_number : int) -> list[Maintenance_request]:
        maintenencereports = []
        all_maintenance_reports = self.dwl.get_all_maintenance_requests_dw()
        for maintenance_report in all_maintenance_reports:
            if maintenance_report.property_number == property_number:
                maintenencereports.append(maintenance_report)
        return maintenencereports
    

   # def update_maintenance_request_logic(id, info_change, what_info):

       # all_requests = DW_Maintenance_request.get_all_maintenance_requests_dw()

       # for request in all_requests[1:]:

       # DW_Maintenance_request.update_maintenance_request_dw(id, info_change, what_info)

    def update_maintenance_logic(self, id , updated_data, what_data: int):

        all_maintenances = self.dwl.get_all_maintenance_requests_dw()
        for maintenance in all_maintenances:
            if id == maintenance.id and maintenance.status != "closed":

                maintenance_change = self.dwl.update_maintenance_request_dw(id, updated_data, what_data)

        if maintenance_change:
            return f"Employee with ID {id} updated successfully."
        else:
            return f"Employee with ID {id} not found."
        
    def add_maintenance_report_logic(self, id, employee_id, report):
        #maintenance_report = DW_Maintenance_request.add_maintenance_report_dw(id, employee_id, report)
        
        all_maintenances = self.dwl.get_all_maintenance_requests_dw()
        for maintenance in all_maintenances:
            if id == maintenance.id:
            
                try:
                    self.dwl.add_maintenance_report_dw(id, employee_id, report)
                    return print("Maintenance report successfully created")
                except RuntimeError as e:
                    print(e)
                

        """if maintenance_report:
            return f"A report for request {id} was created successfully."
        else:
            return f"Request with ID {id} not found."""

    def approve_maintenace_report_logic(self, id):
        #maintenance_report = DW_Maintenance_request.add_approve_maintenance_report_dw(id)

        """if maintenance_report:
            return f"A report {id} was closed successfully."
        else:
            return f"Request with ID {id} not found."""

        all_maintenances = self.dwl.get_all_maintenance_requests_dw()

        for maintenance in all_maintenances:
            if id == maintenance.id and maintenance.status == "Ready":
                try:
                    self.dwl.add_approve_maintenance_report_dw(id)
                    return "Maintenance Report successfully approved"
                except:
                    pass
        raise f"Report with id: {id} can not be found"
        #return print(f"Report with id: {id} can not be found")