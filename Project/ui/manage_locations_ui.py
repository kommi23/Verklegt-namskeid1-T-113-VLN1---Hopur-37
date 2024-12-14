import os
from logic.logic_wrapper import DataLayerWrapper
from Models.Location import Location

class Manage_Locations:

    def __init__(self, llw):
         self.llw = llw

    def display_Locations(self): #virkar
            locations = []
            locations = self.llw.list_all_locations()
                
            if not locations:
                print("No locations found.")

            else:
                for i in locations:
                    print(i)