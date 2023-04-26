#!/usr/bin/env python3
import sqlite3

from database import *


def populateFighters(file):
    file = open(file)
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            fighter = line.split(",")
            # print(fighter)
            insertFighter(*fighter)
        i += 1
    file.close()


def populateFights(file, test_db="../database/database.db"):
    file = open(file)
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            fight = line.split(",")
            # print(fighter)
            connection = sqlite3.connect(test_db)
            cursor = connection.cursor()
            winnerId = fight[1]
            loserId = fight[2]
            try:
                cursor.execute("SELECT MAX(fight_id) FROM Fight")
                id = cursor.fetchone()[0]
                if id is not None:
                    id = id + 1
                else:
                    id = 1

                cursor.execute("""
                INSERT INTO Fight (fight_id, winner_id, loser_id)
                VALUES(?,?, ?)
                """, (id, winnerId, loserId))
                connection.commit()

                cursor.execute(("""UPDATE Fighter SET wins = wins + 1
                WHERE fighter_id = ?"""), (winnerId,))
                connection.commit()
                cursor.execute(("""UPDATE Fighter SET losses = losses + 1
                WHERE fighter_id = ?"""), (loserId,))
                connection.commit()
                print("Added Fight between", winnerId, "and", loserId)

            except Exception as e:
                print("Fight Table Does not exist", e)
            finally:
                connection.close()
        i += 1
    file.close()


def populateCoaches(file):
    file = open(file)
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            coach = line.split(",")
            # print(fighter)
            insertCoach(*coach)
        i += 1
    file.close()


def populateRounds(file):
    file = open(file)
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            round = line.split(",")
            # print(fighter)
            insertRound(*round)
        i += 1
    file.close()


def populateTournaments(file):
    file = open(file)
    i = 0
    for line in file:
        if i == 0:
            pass
        else:
            tournament = line.split(",")
            insertTournament(*tournament)
        i += 1
    file.close()

# populateFighters("../data/fighters.csv")
