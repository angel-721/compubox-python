#!/usr/bin/env python3
from database import *

"""
Inputs are a single line of values separated by commas  e.g: Angel, 80, 90, 20, 0, 4, True, 0
"""


def addFighter(hint):
    if (hint != 0):
        print("name,height,reach,wins,losses,draws,was_champion,coach_id")
    fighter = input("Input a fighter: ")
    fighter = fighter.split(",")
    insertFighter(*fighter)


def addCoach(hint):
    if (hint != 0):
        print("name")
    coach = input("Input a coach: ")
    coach = coach.split(",")
    insertCoach(*coach)


def addFight(hint):
    if (hint != 0):
        print("red-fighter,blue-fighter,winner")
    fight = input("Input a fight: ")
    fight = fight.split(",")
    if fight[2].lower() == "red":
        winner = True
    else:
        winner = False
    insertFight(fight[0], fight[1], winner)


def addRound(hint):
    if (hint != 0):
        print("fight-id,red-punch-count,blue-punch-count")
        selectFights()
    round = input("Input a round: ")
    round = round.split(",")
    insertRound(*round)
