from data.data_wrapper import DataLayerWrapper
from Models.Property import *



class Property_logic():
    def __init__(self, datawrapper : DataLayerWrapper):
        self.dwl : DataLayerWrapper = datawrapper


    def add_property(self, property):
        all_properties = self.dwl.get_all_properties_dw()

        for existing_property in all_properties:
            if existing_property.property_id == property.property_id:
                return print(f"A property with the id: {property.property_id} already exists.")
            
        all_locations = self.dwl.get_all_locations()
        for location in all_locations:
            if location.location == property.location:
                self.dwl.add_property_dw(property)
                return "property has been added"
            ret = f"The location {property.location} does not exist in the system."
        return ret 

   
    def get_all_proberties_logic(self):
        return self.dwl.get_all_properties_dw()
    

    def get_properties_by_location_data_logic(self, location):
        return self.dwl.get_property_by_location_dw(location)


    def change_property(self, id, info_change, what_info):
        all_properties = self.dwl.get_all_properties_dw()
        for property in all_properties:
            if id == property.property_id:
                try:
                    self.dwl.update_property_dw(id, info_change, what_info)
                    return "Property successfully updated"
                except:
                    pass
        ret = f"Property with id: {id} can not be found"
        return ret

#1

