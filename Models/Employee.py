class Employee:
    """docstring for Employee"""
    def __init__(self, employee_id: str, name: str, location: str, phone: str, email: str, address: str):
        self.employee_id = employee_id
        self.name = name
        self.location = location
        self.phone = phone
        self.email = email
        self.address = address

    def toCSVList(self) -> list:
        return [self.employee_id, self.name, self.location, self.phone, self.email, self.address]
    
    def toCommastring(self) -> str:
        return f"{self.employee_id},{self.name},{self.location},{self.phone},{self.email},{self.address}\n"

