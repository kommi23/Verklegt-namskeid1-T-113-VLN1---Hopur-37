from employee_data import EmployeeData 
from contractorreport_data import ContractorReport
from location_data import LocationData
from maintanencereport_data import MaintenanceReportData
from maintenance_data import MaintenanceData
from property_data import ProbertyData


def get_employee(employee_id = "2203792244"):
    print(EmployeeData.get_singular_employee(employee_id))

def get_employees(self):
    print(EmployeeData.get_employees(self))


get_employee()
print("")
print("")
self = "" 
get_employees(self)