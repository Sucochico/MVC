# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:01:27 2023

@author: lab
"""

class Robotmodel:
    def __init__(self, elevation, rotation, lenght):
        self.elevation = 0
        self.rotation = 0
        self.lenght = 0
        
    def move_elevation(self, elevation):
        self.elevation = elevation
        print(f"moving elevation to {elevation} degreees")
        
    def move_rotation(self, rotation):
        self.rotation = rotation
        print(f"moving rotation to {rotation} degreees")
        
    def move_lenght(self, lenght):
        self.lenght = lenght
        print(f"moving lenght to {lenght} degreees")
        
    def stop_movement(self):
        print("Stopping movement")
        
        
        