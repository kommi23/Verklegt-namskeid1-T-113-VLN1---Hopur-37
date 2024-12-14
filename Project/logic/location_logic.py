from data.data_wrapper import DataLayerWrapper

class Location_logic:
    def __init__(self, datawrapper: DataLayerWrapper):
        self.dwl = datawrapper

    def get_location_list(self):
        return self.dwl.get_all_locations()
    