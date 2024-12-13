from data.data_wrapper import *
from Models.Property import *


class Property_logic():
    def add_property(property):
        all_properties = DW_properties.get_all_properties_dw()

        for existing_property in all_properties:
            if existing_property.property_id == property.property_id:
                return print(f"A property with the id: {property.property_id} already exists.")
            
        all_locations = DW_Location.get_all_locations()
        for location in all_locations:
            if location.location == property.location:
                DW_properties.add_property_dw(property)
                return print("property has been added")
        return print(f"The location {property.location} does not exist in the system.")

   
    def get_all_proberties_logic():
        return DW_properties.get_all_properties_dw()
    

    def get_properties_by_location_data_logic(location):
        return DW_properties.get_property_by_location_dw(location)


    def change_property(id, info_change, what_info):
        all_properties = DW_properties.get_all_properties_dw()
        for property in all_properties:
            if id == property.property_id:
                try:
                    DW_properties.update_property_dw(id, info_change, what_info)
                    return print("Property successfully updated")
                except:
                    pass
        return print(f"Property with id: {id} can not be found")

#1

