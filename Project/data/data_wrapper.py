from employee_data import EmployeeData 
from contractorreport_data import ContractorReport
from location_data import LocationData
from maintanencereport_data import MaintenanceReportData
from maintenance_data import MaintenanceData
from property_data import ProbertyData

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
     
    def change_employee_name(employee_id, new_name):
        x = EmployeeData.employee_change_name(employee_id, new_name)
        if x == True:
            print("success")
        else: print(":(")

    def change_employee_email(employee_id, new_email):
        x = EmployeeData.employee_change_email(employee_id, new_email)
        if x == True:
            print("success")
        else: print(":(")

    def change_employee_work_phone(employee_id, new_work_phone):
        x = EmployeeData.employee_change_work_phone(employee_id, new_work_phone)
        if x == True:
            print("success")
        else: print(":(")

    def change_employee_personal_phone(employee_id, new_personal_phone):
        x = EmployeeData.employee_change_personal_phone(employee_id, new_personal_phone)
        if x == True:
            print("success")
        else: print(":(")

    def change_employee_address(employee_id, new_address):
        x = EmployeeData.employee_change_address(employee_id, new_address)
        if x == True:
            print("success")
        else: print(":(")

    def change_employee_location(employee_id, new_location):
        x = EmployeeData.employee_change_location(employee_id, new_location)
        if x == True:
            print("success")
        else: print(":(")




class dw_contractors:

    pass
    

#x = dw_employee



employee_id = "2203792244"
new_name = "King Theoden"
dw_employee.change_employee_name(employee_id, new_name)


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