# -*- coding: utf-8 -*-
"""
Created on Tue May  2 10:16:09 2023

@author: lab

"""

from robot_model import Robotmodel
from robot_view import RobotView
from robot_controller import RobotController 

model=Robotmodel(0,0,0)
view=RobotView()
controller=RobotController(model, view)
controller.run()