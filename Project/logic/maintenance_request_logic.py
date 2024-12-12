from data.data_wrapper import *
from Models.Maintenance_request import *

class Maintenance_request_logic:
    def add_maintenance_request_logic(new_request):
        all_requests = DW_Maintenance_request.get_all_maintenance_requests_dw()

        for request in all_requests:
            if request.id == new_request.id:
                raise RuntimeError(f"A maintenance reqeust with the id {new_request.id} already exists")
        
        return DW_Maintenance_request.add_maintenance_request_dw(new_request)
    
    def get_all_maintenance_requests_logic():
        return DW_Maintenance_request.get_all_maintenance_requests_dw()
    
    def get_maintenance_request_by_id_logic(maintenance_id):
        return DW_Maintenance_request.get_all_maintenance_requests_dw(maintenance_id)

    def get_maintenance_request_by_property_id_logic(property_id):
        return DW_Maintenance_request.get_maintenance_request_by_property_id_dw(property_id)
    
    def get_maintenance_request_by_employee_id_logic(employee_id):
        return DW_Maintenance_request.get_maintenance_request_by_employee_id_dw(employee_id)
    

    def get_maintenancereports_by_employee(employee_id: int) -> list[Maintenance_request]:
        """Returns a list of all MaintenanceReports that the employee is registered to.
        """
        maintenencereports = []
        all_maintenance_reports = DW_Maintenance_request.get_all_maintenance_requests_dw()
        for maintenance_report in all_maintenance_reports:
            if maintenance_report.employee_id == employee_id:
                maintenencereports.append(maintenance_report)
        return maintenencereports
