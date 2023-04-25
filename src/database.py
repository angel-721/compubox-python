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
            """SELECT MAX(round_number) FROM Round WHERE fight_id = ?;""",
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


""" quarter, semi, and final are all fight_ids """


def insertTournament(name, quarterA, quarterB,
                     semiA, semiB, finalFight,
                     test_db='../database/database.db'):

    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT MAX(tournament_id) FROM Tournament")
        id = cursor.fetchone()[0]
        if id is not None:
            id = id + 1
        else:
            id = 1

        cursor.execute("""
        INSERT INTO Tournament (tournament_id, tournament_name,
        quarter_finals_a_id, quarter_finals_b_id, 
        semi_finals_a_id, semi_finals_b_id,
        final_fight_id)
        VALUES(?,?,?,?,?,?,?)
        """, (id, name, quarterA, quarterB, semiA, semiB, finalFight))
        connection.commit()
        print("Added Tournament:", name, "to Tournament")

        # Add the winner of the final fight to the champion table
        champ = cursor.execute(
            """SELECT * FROM Fight WHERE fight_id = ?;""", (finalFight)
        ).fetchall()
        champId = champ[0][1]

        insertChampion(champId, id)

        # Update Fighter Table to set the fighter to a champion
        cursor.execute(("""UPDATE Fighter SET was_champion = 1
        WHERE fighter_id = ?"""), (champId,))
        connection.commit()

    except Exception as e:
        print("Tournament Table Does not exist", e)
        return
    finally:
        connection.close()
    return


def insertChampion(fighterId, tournamentId,
                   test_db='../database/database.db'):

    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT MAX(champion_id) FROM Champion")
        id = cursor.fetchone()[0]
        if id is not None:
            id = id + 1
        else:
            id = 1

        cursor.execute("""
        INSERT INTO Champion (champion_id, fighter_id,
        tournament_id) 
        VALUES(?,?,?)
        """, (id, fighterId, tournamentId))
        connection.commit()
        print("Added Champion:", fighterId, "to Champion")
    except Exception as e:
        print("Champion Table Does not exist", e)
        return
    finally:
        connection.close()
    return


"""Basic SELECT functions are just helpers"""


def selectFights(test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        query = cursor.execute(
            """SELECT * FROM FIGHT"""
        ).fetchall()
        # print(query)
        print("Here is a list of fight ids: ")
        for fight in query:
            print(fight[0])
        connection.commit()
    except Exception as e:
        print("Fight Table Does not exist", e)
        return
    finally:
        connection.close()
    return


def selectFighters(test_db='../database/database.db'):
    connection = sqlite3.connect(test_db)
    cursor = connection.cursor()
    try:
        query = cursor.execute(
            """SELECT * FROM FIGHTER"""
        ).fetchall()
        # print(query)
        print("Here is a list of fighters: ")
        for fighter in query:
            print(fighter[1])
        connection.commit()
    except Exception as e:
        print("Fighter Table Does not exist", e)
        return
    finally:
        connection.close()
    return
