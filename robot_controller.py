# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class RobotController:
    def __init__(self, mode1, view):
        self.mode1 = mode1
        self.view = view
    
    def run(self):
        while True:
            command = input("Enter a command(move or stop):")
            if command =="move":
                elevation, rotation, lenght = self.view.get_user_input()
                self.mode1.move_elevation(elevation)
                self.mode1.move_rotation(rotation)
                self.mode1.move_lenght(lenght)
            elif command =="stop":
                self.mode1.stop_movement()
                break
            else:
                self.view.show_error_message("error")
            
