class Employee:
    def __init__(self, employee_id, name, social_security_number, address, landline, mobile_phone, email, location):
        self.employee_id = employee_id
        self.name = name
        self.social_security_number = social_security_number
        self.address = address
        self.landline = landline
        self.mobile_phone = mobile_phone
        self.email = email
        self.location = location


class Manager:
    def __init__(self, manager_id, name, social_security_number, address, landline, mobile_phone, email, location):
        self.manager_id = manager_id
        self.name = name
        self.social_security_number = social_security_number
        self.address = address
        self.landline = landline
        self.mobile_phone = mobile_phone
        self.email = email
        self.location = location

class Contractor:
    def __init__(self, name, contact_name, location, phone, address, opening_hours):
        self.name = name
        self.contact_name = contact_name
        self.location = location
        self.phone = phone
        self.address = address
        self.opening_hours = opening_hours

