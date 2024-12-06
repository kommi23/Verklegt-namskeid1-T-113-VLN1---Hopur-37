from data.employee_data import EmployeeData 
from data.contractorreport_data import ContractorReport
from data.location_data import LocationData
from data.maintanencereport_data import MaintenanceReportData
from data.maintenance_data import MaintenanceData
from data.property_data import ProbertyData

class dw_employee:
    def get_employee(employee_id = "2203792244"):
        # return EmployeeData.get_singular_employee(employee_id)

            #############test kóði################
        print(EmployeeData.get_singular_employee(employee_id))

    def get_employees():
        return EmployeeData.get_employees()

        #############test kóði################
       #print(EmployeeData.get_employees())

    #placeholder
    #employee = ["name", "employee_id", "email", "address", "work_phone", "personal_phone", "location"]

    def write_employee(employee):
        
        #############test kóði################
        x = EmployeeData.add_employee(employee)
        if x == True:
            print("success")
        else: print(":(")


    #2203792244, Jacob Yxa, jacob.yxa@nanair.is, Vei 224 3B Longyearbyen, +47 92 09 77 01, +354 777 1338, Svalbard

    employee_id = "2203792244"
    def delete_employee(employee_id):
        x = EmployeeData.delete_employee(employee_id)
        if x == True:
            print("success")
        else: print(":(")
     

    

#############test kóði################ 
#get_employee()
#print("")
#print("")
#self = "" 
#get_employees(self)
#print("")
#print("")
#write_employee(self,employee)
"""
self = "" 
get_employees(self)
delete_employee(employee_id)
get_employees(self)
"""
#####################################