
class Employee:
    def __init__(self, employee_id:int, name:str, social_security_number:int, address:str, landline:int, mobile_phone:int, email:str, location:str):
        self.employee_id = employee_id
        self.name = name
        self.social_security_number = social_security_number
        self.address = address
        self.landline = landline
        self.mobile_phone = mobile_phone
        self.email = email
        self.location = location

    def __iter__():
        for attr in vars().items():
            yield attr


alex_as_employee = Employee(1, "Alex", 6464, "Heima 1", 553, 615, "alex@ru.is", "iceland" )

alex_as_list = []

for i in alex_as_employee:
    alex_as_list.append(i)

print(alex_as_list)

#print(alex_as_employee.employee_id)


