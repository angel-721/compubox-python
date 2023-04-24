#!/usr/bin/env python
import sqlite3


def insertFighter(name, height, reach, wins, losses, draws, wasChampion, coachId, test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT MAX(fighter_id) FROM Fighter")
        id = cursor.fetchone()[0]
        if id is not None:
            id = id + 1
        else:
            id = 1

        cursor.execute("""
        INSERT INTO Fighter (fighter_id, name, height,
        reach, wins, losses, draws, was_champion, coach_id)
        VALUES(?,?,?,?,?,?,?,?, ?)
        """, (id, name, height, reach, wins, losses,
              draws, wasChampion, coachId))
        connection.commit()
        print("Added Fighter", name)
    except Exception as e:
        print("Fighter Table Does not exist", e)
        return
    finally:
        connection.close()
    return


def insertCoach(name, test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
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
        """, (id, name))
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


def insertFight(redFighter, blueFighter, winner, test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()

    try:
        table = cursor.execute("""
        SELECT fighter_id FROM Fighter WHERE name = ?;
        """, (redFighter,)).fetchall()
        redID = table[0][0]
    except Exception as e:
        print(redFighter, "Does not exist", e)
        return

    try:
        table = cursor.execute("""
        SELECT fighter_id FROM Fighter WHERE name = ?;
        """, (blueFighter,)).fetchall()
        blueID = table[0][0]
    except Exception as e:
        print(blueFighter, "Does not exist", e)
        return

    winner = bool(winner)
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
        """, (id, winnerId, loserId))
        connection.commit()

        cursor.execute(("""UPDATE Fighter SET wins = wins + 1
        WHERE fighter_id = ?"""), (winnerId,))
        connection.commit()
        cursor.execute(("""UPDATE Fighter SET losses = losses + 1
        WHERE fighter_id = ?"""), (loserId,))
        connection.commit()
        print("Added Fight between", redFighter, "and", blueFighter)

    except Exception as e:
        print("Fight Table Does not exist", e)
    finally:
        connection.close()
    return


def insertRound(fightId, redPunchCount, bluePunchCount, test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        cursor.execute(
            """SELECT MAX(round_number) FROM Round WHERE fight_id = ?""",
            (fightId,)
        )
        roundNum = cursor.fetchone()[0]
        if roundNum is not None:
            roundNum = roundNum + 1
        else:
            roundNum = 1

        cursor.execute("SELECT MAX(round_id) FROM Round")
        id = cursor.fetchone()[0]
        if id is not None:
            id = id + 1
        else:
            id = 1

        cursor.execute("""
        INSERT INTO Round (round_id, round_number, fight_id,
        punches_r_landed, punches_b_landed)
        VALUES(?,?,?,?,?)
        """, (id, roundNum, fightId, redPunchCount, bluePunchCount))
        connection.commit()
        print("Added Round number", roundNum, "to fight", fightId)
    except Exception as e:
        print("Round Table Does not exist", e)
        return
    finally:
        connection.close()
    return


def selectFights(test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        query = cursor.execute(
            """SELECT * FROM FIGHT"""
        ).fetchall()
        print(query)
        connection.commit()
    except Exception as e:
        print("Fight Table Does not exist", e)
        return
    finally:
        connection.close()
    return
