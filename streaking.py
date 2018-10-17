# -*- coding: utf-8 -*-
"""

@author: Allan Li, Sunnie Ma
"""
import opentrons
from opentrons import labware, instruments, robot

#This is the radius of the dish in centermeters
radius=4.5

tiprack = labware.load('tiprack-10ul', '1')
bacteria = labware.load('96-flat', '4')
dish = labware.load('96-PCR-flat', '5')

p = instruments.P300_Single(
		mount='right',
		tip_racks=[tiprack])

dishInfo=dish.wells('A1').top()[0]

n=radius/5

center_x=dish.wells('A1').top()[1][0]
center_y=dish.wells('A1').top()[1][1]-40
z=dish.wells('A1').top()[1][2]-3



#adjust the coordinates of the dish

#function that moves to a specific point of the dish
def move(x,y):
    x=n*x
    y=n*y
    tempVector=opentrons.util.vector.Vector(x+center_x, y+center_y, z)
    p.move_to((dishInfo,tempVector),strategy='direct')
    
#creates a coordinate for the move_to function
def coordinate(x_1,y_1,z_1):
    x_1=n*x_1
    y_1=n*y_1
    return(dishInfo,opentrons.util.vector.Vector(x_1+center_x, y_1+center_y, z_1))

#streaking in the second quadrant
def main1():
     move(-40,0)
     move(0,40)
     move(-30,0)
     move(0,30)
     move(-20,0)
     move(0,20)
     move(-10,0)
     move(0,10)
#streaking in the first quadrant   
def main2():
    move(-20,20)
    move(10,0)
    move(5,10)
    move(20,0)
    move(5,20)
    move(30,0)
    move(5,30)
    move(40,0)
#streaking in the forth quadrant    
def main3():
    move(40,10)
    move(0,-40)
    move(30,-5)
    move(0,-30)
    move(20,-5)
    move(0,-20)
    move(10,-5)
    move(0,-10)
    move(5,-5)
#streaking in the third quadrant    
def main4():
    move(10,-10)
    move(-10,-5)
    move(-5,-10)
    move(-20,-5)
    move(-5,-20)
    move(-30,-5)
    move(-5,-30)
    move(-40,-5)
    move(-5,-40)
#--------------------------
##dip in bacteria, step 1
p.pick_up_tip()
p.aspirate(1, bacteria.wells('A1').top()) 
p.touch_tip(bacteria.wells('A1'))
p.move_to(coordinate(-40,0,10))
main1()
p.drop_tip()

#step 2
p.pick_up_tip()
p.move_to(coordinate(-20,20,10))
p.aspirate(1, coordinate(-20,20,10)) 
main2()
p.drop_tip()
#step 3
p.pick_up_tip()
p.move_to(coordinate(40,10,3))
main3()
p.drop_tip()
#step 4
p.pick_up_tip()
p.move_to(coordinate(10,-10,3))
main4()
p.drop_tip()