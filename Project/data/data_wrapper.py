from data.employee_data import EmployeeData 
from data.property_data import PropertyData
from data.location_data import LocationData
#from contractorreport_data import ContractorReport
#from location_data import LocationData
#from maintanencereport_data import MaintenanceReportData
#from maintenancerequests_data import MaintenanceRequestData
#from contractor_data import ContractorData


class DW_employee:

    def write_employee_dw(employee): 
        
        x = EmployeeData.write_employe_data(employee) 
        if x == True:
            print("success")
        else: print(":(")

    def get_singular_employee_dw(employee_id):
        return EmployeeData.get_singular_employee_data(employee_id)


    def get_employees_dw() -> list:    
        return EmployeeData.get_employees_data()

        #############test kóði################
       #print(EmployeeData.get_employees())

    #placeholder
    #employee = ["name", "employee_id", "email", "address", "work_phone", "personal_phone", "location"]

    def get_employees_location_dw(location):
        return EmployeeData.get_employees_location_data(location)


    def delete_employee_dw(employee_id):
        x = EmployeeData.delete_employee_data(employee_id)
        if x == True:
            print("success")
        else: print(":(")


    def update_employee_dw(employee_id,updated_data, what_data):
        return EmployeeData.update_employee_data(employee_id, updated_data, what_data)



    #2203792244, Jacob Yxa, jacob.yxa@nanair.is, Vei 224 3B Longyearbyen, +47 92 09 77 01, +354 777 1338, Svalbard


class DW_properties:

    def get_all_properties_dw():
        return PropertyData.get_proberty_data()
    
    def get_property_by_number_dw(number):
        return PropertyData.get_singular_property_data(number)
    
    def get_property_by_location_dw(location):
        return PropertyData.get_properties_by_location_data(location)
    
    #def get_property_by_contractor_report() #þarf að hugsa þetta

    def add_property_dw(property):
        return PropertyData.add_property_data(property)
    
    #þarf að bæta við fasteign

    def delete_property_dw(property_number):
        return PropertyData.delete_property_data(property_number)

class DW_Location:
    
    def update_location_data(property_number, updated_data, what_data): 
        return LocationData.update_location_data(property_number, updated_data, what_data)