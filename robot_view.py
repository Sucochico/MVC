# -*- coding: utf-8 -*-
"""
Created on Tue May  2 09:42:37 2023

@author: lab
"""

class RobotView:
    def get_user_input(self):
        elevation=int(input("ingrese el valor de la elevacion en grados: "))
        rotation=int(input("ingrese el valor de la rotacion en grados: "))
        length=int(input("ingrese el valor de la longitud en metros: "))
        return elevation,rotation,length
    
    def show_error_message(self,message):
        print("error: (message)")
        
        
    