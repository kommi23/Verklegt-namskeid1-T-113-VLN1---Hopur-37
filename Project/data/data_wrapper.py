from employee_data import EmployeeData 
from contractorreport_data import ContractorReport
from location_data import LocationData
from maintanencereport_data import MaintenanceReportData
from maintenance_data import MaintenanceData
from property_data import PropertyData
from contractor_data import ContractorData

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
     
    def change_employee_data(employee_id,updated_data, what_data):
        x = EmployeeData.employee_change_name(employee_id, updated_data, what_data)
        if x == True:
            print("success")
        else: print(":(")
        

class dw_contractors:

    def get_contractor(contractor):
        return ContractorData.get_singular_contractor(contractor)
    
    def get_contractors():
        return ContractorData.get_contractors()
    
    def write_contractor(contractor):
        return ContractorData.add_contractor(contractor)

    def get_contractors_by_location(location):
        return ContractorData.get_contractor_by_location(location)

class dw_properties:

    def get_all_properties():
        return PropertyData.get_proberty()
    
    def get_property_by_number(number):
        return PropertyData.get_singular_property(number)
    
    def get_property_by_location(location):
        return PropertyData.get_properties_by_location(location)
    
    #def get_property_by_contractor_report() #þarf að hugsa þetta

    def add_property(property):
        return PropertyData.add_property(property)
    
    #þarf að bæta við fasteign

    def delete_property(property_number):
        return PropertyData.delete_property(property_number)


    

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