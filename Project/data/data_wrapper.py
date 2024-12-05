from employee_data import EmployeeData 
from contractorreport_data import ContractorReport
from location_data import LocationData
from maintanencereport_data import MaintenanceReportData
from maintenance_data import MaintenanceData
from property_data import ProbertyData


def get_employee(employee_id = "2203792244"):
    # return EmployeeData.get_singular_employee(employee_id)

           #############test kóði################
    print(EmployeeData.get_singular_employee(employee_id))

def get_employees(self):
    # return EmployeeData.get_employees(self)

    #############test kóði################
    print(EmployeeData.get_employees(self))

#placeholder
employee = ["name", "employee_id", "email", "address", "work_phone", "personal_phone", "location"]

def write_employee(self,employee):
    
    #############test kóði################
    x = EmployeeData.add_employee(self, employee)
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
self = "" 
get_employees(self)
delete_employee(employee_id)
get_employees(self)
#####################################