class Property_logic():
    def add_property(property):
        all_properties = DW_properties.get_all_properties_dw()

        for existing_property in all_properties:
            if existing_property.property_number == property.property_number:
                raise RuntimeError("Property with ID {property.id} already exists")
        
        DW_properties.add_property_dw(property)

from data.data_wrapper import *