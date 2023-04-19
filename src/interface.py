#!/usr/bin/env python3
from database import *

"""
Inputs are a single line of values seperated by commas  e.g: Angel, 80, 90, 20, 0, 4, True, 0
"""
def addFighter(hint):
    if(hint != 0): print("name,height,reach,wins,losses,draws,was_champion,coach_id")
    fighter = input("Input a fighter: ")
    fighter = fighter.split(",")
    insertFighter(*fighter)

def addCoach(hint):
    if(hint != 0): print("name")
    coach = input("Input a coach: ")
    coach = coach.split(",")
    insertCoach(*coach)
