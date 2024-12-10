class LL_employee():
    # Setur inn allar upplýsingar um employee og ég gef til baka streng sem segir til um hvort það hafi tekist að skrá hann
    def add_employee(new_employee) -> str:
        return Employee_logic.write_employee_logic(new_employee)
    
    # Ekkert input, færð bara lista af öllum eployees
    def get_employee_list(self) -> list:
        return Employee.get_employee_list
    
    # Tekur inn id til að sjá hvern er verið að updatea, nýja variablið inn í updated_data sem getur verið strengur eða int og 
    # Síðan læturu vita hvað er verið að vinna með með þvi að setja inn númeirð sem representar hvar í listanum breytingin 
    # er (nafn = 1, gsm = 3...). Svo færð þú til baka streng sem segir hvort það hafi tekist
    def update_employee(self, id: int, updated_data, what_data: int) -> str:
        return Employee.update_employee(id, updated_data, what_data)
    
    # Put in the name of the employee and I will return a list of all the info we have about that employee
    def search_employee_name(self, name: str) -> list:
        return Employee.search_employee_name(name)
    
    # Put in the id of the employee and I will return a list of all the info we have about the employee
    def search_employee_id(self, id: int) -> list:
        return Employee.search_employee_id(id)
    
    # Put in the name of the location and I will pull upp a list with all the employees that work there and their information
    def search_employee_location(self, location: str) -> list:
        return Employee.search_employee_location(location)
    
class LL_contractor:
    def get_contractor_list() -> list:
        return Contractor.get_contractor_list()
    
    def add_contractor(contractor: list):
        Contractor.add_contractor(contractor)

    def update_contractor(id: int, updated_data, what_data: int):
        Contractor.update_contractor(id, updated_data, what_data)

    def add_contractor_review(id: int, review: str):
        Contractor.add_contractor_review(id, review)

    def get_contractor_review(id) -> list :
        return Contractor.get_contractor_review
    
    def search_contractor_history(id) -> list:
        return Contractor.search_contractor_maintainance_history(id)
        
class LL_property():
     def add_property(property):
        Property_logic.add_property(property)
        

    
    
from logic.employee_logic import *
from logic.contractor_logic import *
from logic.property_logic import *
from Models.Employee import *