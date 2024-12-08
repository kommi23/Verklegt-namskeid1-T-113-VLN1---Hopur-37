class ll_employee():
    # Setur inn allar upplýsingar um employee og ég gef til baka streng sem segir til um hvort það hafi tekist að skrá hann
    def add_employee(id: int, name: str, location: str, phone_number: int, email: str, address: str) -> list:
        return Employee.add_employee(Employee.turn_into_list(id, name, location, phone_number, email, address))
    
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
    
from Project.logic.employee_logic import *