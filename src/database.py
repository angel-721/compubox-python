#!/usr/bin/env python
import sqlite3

def insertFighter(name, height, reach, wins, losses, draws, wasChampion, coachId):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT MAX(fighter_id) FROM Fighter")
        id = cursor.fetchone()[0]
        if id is not None:
            id = id + 1
        else:
            id = 1

        cursor.execute("""
        INSERT INTO Fighter (fighter_id, name, height, reach, wins, losses, draws, was_champion, coach_id)
        VALUES(?,?,?,?,?,?,?,?, ?)
        """,(id, name, height, reach, wins, losses, draws, wasChampion,coachId))
        connection.commit()
        print("Added Fighter", name)
    except Exception as e:
        print("Fighter Table Does not exist", e)
        return
    finally:
        connection.close()
    return

def insertCoach(name):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT MAX(coach_id) FROM Coach")
        id = cursor.fetchone()[0]
        if id is not None:
            id = id + 1
        else:
            id = 1

        cursor.execute("""
        INSERT INTO Coach (coach_id, name)
        VALUES(?,?)
        """,(id, name))
        connection.commit()
        print("Added Coach", name)
    except Exception as e:
        print("Coach Table Does not exist", e)
        return
    finally:
        connection.close()
    return

"""
winner true then red wins, winner false then blue wins
"""
def insertFight(redFighter, blueFighter, winner):
    connection = sqlite3.connect('../database/database.db')
    cursor = connection.cursor()

    try:
        table = cursor.execute("""
        SELECT fighter_id FROM Fighter WHERE name = ?;
        """,(redFighter,)).fetchall()
        redID = table[0][0]
        print(redID)
    except:
        print(redFighter, "Does not exist")
        return

    try:
        table = cursor.execute("""
        SELECT fighter_id FROM Fighter WHERE name = ?;
        """,(blueFighter,)).fetchall()
        blueID = table[0][0]
    except:
        print(blueFighter, "Does not exist")
        return

    if winner:
        winnerId, loserId = redID, blueID
    else:
        winnerId, loserId = blueID, redID

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
        """,(id,winnerId, loserId))
        connection.commit()
        print("Added Fight between", redFighter, "and", blueFighter)
    except Exception as e:
        print("Fight Table Does not exist", e)
    finally:
        connection.close()
    return

