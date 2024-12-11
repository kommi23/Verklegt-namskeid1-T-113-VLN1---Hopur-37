from data.employee_data import EmployeeData 
from data.property_data import PropertyData
from data.location_data import LocationData


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

    def get_employees_location_dw(location):
        return EmployeeData.get_employees_location_data(location)


    def delete_employee_dw(employee_id):
        x = EmployeeData.delete_employee_data(employee_id)
        if x == True:
            print("success")
        else: print(":(")


    def update_employee_dw(employee_id,updated_data, what_data):
        return EmployeeData.update_employee_data(employee_id, updated_data, what_data)

class DW_properties:

    def get_all_properties_dw():
        return PropertyData.get_all_proberties_data()
    
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
    
    def update_property_dw(id, info_change, what_info):
        PropertyData.update_property_data(id, info_change, what_info)

class DW_Location:
    
    def get_all_locations_dw():
        return LocationData.get_locations_data()