class Location:
    def __init__(self, location, country, airport, phone_number, opening_time, manager):
        self.location = location
        self.country = country
        self.airport = airport
        self.phone_number = phone_number
        self.opening_time = opening_time
        self.manager = manager

    def turn_location_into_list(self):
        return [self.location, self.country, self.airport, self.phone_number, self.opening_time, self.manager]
    
    def __str__(self) -> str:
        return f"[{self.location} {self.country} {self.airport} {self.phone_number} {self.opening_time} {self.manager}]"