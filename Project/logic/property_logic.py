class Property_logic():
    def add_property(property):
        all_properties = DW_properties.get_all_properties_dw()

        for existing_property in all_properties:
            if existing_property.property_number == property.property_number:
                raise RuntimeError("Property with ID {property.id} already exists")
        
        DW_properties.add_property_dw(property)
    
    def get_all_proberties_logic():
        return DW_properties.get_all_properties_dw()
    

    def get_properties_by_location_data_logic(location):
        return DW_properties.get_property_by_location_dw(location)


    def change_property(id, info_change, what_info):
        DW_properties.update_property_dw(id, info_change, what_info)
                

from data.data_wrapper import *