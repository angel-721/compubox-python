#!/usr/bin/env python3
import pytest
import sqlite3
import os.path
import shutil
import database as db

DB_FILE = "tests.db"

def describe_compubox():

    @pytest.fixture(autouse=True)
    def test_db():
        current_file_path = os.path.abspath(__file__)
        project_root = os.path.dirname(os.path.dirname(current_file_path))
        src_db = os.path.join(project_root, "database", "database.db")
        shutil.copy(src_db, DB_FILE)
        yield DB_FILE
        os.remove(DB_FILE)

    @pytest.fixture(autouse=True)
    def cursor_connection(test_db):
        connection = sqlite3.connect(test_db)
        cursor = connection.cursor()
        yield cursor
        cursor.close()
        connection.close()

    @pytest.fixture
    def no_fighter_table(test_db, cursor_connection):
        cursor_connection.execute("DROP TABLE IF EXISTS Fighter")
        cursor_connection.connection.commit()
    @pytest.fixture
    def no_coach_table(test_db, cursor_connection):
        cursor_connection.execute("DROP TABLE IF EXISTS Coach")
        cursor_connection.connection.commit()
    @pytest.fixture
    def no_round_table(test_db, cursor_connection):
        cursor_connection.execute("DROP TABLE IF EXISTS Round")
        cursor_connection.connection.commit()
    @pytest.fixture
    def no_fight_table(test_db, cursor_connection):
        cursor_connection.execute("DROP TABLE IF EXISTS Fight")
        cursor_connection.connection.commit()
    @pytest.fixture
    def no_tournament_table(test_db, cursor_connection):
        cursor_connection.execute("DROP TABLE IF EXISTS Tournament")
        cursor_connection.connection.commit()

    @pytest.fixture
    def red_fighter():
        red_fighter = {
            "name": "red",
            "height": "80",
            "reach": "90",
            "wins": "20",
            "losses": "20",
            "draws": "20",
            "was_champion": "0",
            "coach_id": "0",
        }
        yield red_fighter

    @pytest.fixture
    def blue_fighter():
        blue_fighter = {
            "name": "blue",
            "height": "80",
            "reach": "90",
            "wins": "20",
            "losses": "20",
            "draws": "20",
            "was_champion": "0",
            "coach_id": "0",
        }
        yield blue_fighter

    def describe_insertFighter():
        def it_adds_new_fighter_to_db(test_db, red_fighter, cursor_connection):
            db.insertFighter(*red_fighter.values(), test_db)
            cursor_connection.execute("SELECT * FROM fighter WHERE name='red'")
            rows = cursor_connection.fetchall()
            fighter = rows[0]
            assert red_fighter["name"] == fighter[1]
        def it_raises_exception_if_table_does_not_exist(test_db, red_fighter, no_fighter_table, capsys):
            db.insertFighter(*red_fighter.values(), test_db)
            captured = capsys.readouterr()
            assert "Table Does not exist" in captured.out

    def describe_insertCoach():
        def it_adds_new_coach_to_db(test_db, cursor_connection):
            db.insertCoach("test_coach", test_db)
            cursor_connection.execute("SELECT * FROM coach WHERE name='test_coach'")
            rows = cursor_connection.fetchall()
            coach = rows[0]
            assert coach[1] == "test_coach"
        def it_raises_exception_if_table_does_not_exist(test_db, no_coach_table, capsys):
            db.insertCoach("test_coach", test_db)
            captured = capsys.readouterr()
            assert "Table Does not exist" in captured.out

    def describe_insertFight():
        def it_adds_new_fight_to_db(test_db, red_fighter, blue_fighter, cursor_connection):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            cursor_connection.execute("SELECT MAX(fight_id) FROM Fight")
            oldId = cursor_connection.fetchone()[0]
            db.insertFight("red", "blue", True, test_db)
            cursor_connection.execute("SELECT MAX(fight_id) FROM Fight")
            newId = cursor_connection.fetchone()[0]
            if oldId is not None:
                assert newId > oldId
            else:
                assert newId == 1
        def it_properly_raises_exception_when_red_fighter_is_not_correct(test_db, blue_fighter, capsys):
            db.insertFighter(*blue_fighter.values(), test_db)
            db.insertFight("red", "blue", True, test_db)
            captured = capsys.readouterr()
            assert "Does not exist" in captured.out
        def it_properly_raises_exception_when_blue_fighter_is_not_correct(test_db, red_fighter, capsys):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFight("red", "blue", True, test_db)
            captured = capsys.readouterr()
            assert "Does not exist" in captured.out
        def it_increments_the_wins_of_the_winning_fighter(test_db, red_fighter, blue_fighter, cursor_connection):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            cursor_connection.execute("SELECT wins FROM fighter WHERE name == 'red'")
            oldWins = cursor_connection.fetchone()[0]
            db.insertFight("red", "blue", True, test_db)
            cursor_connection.execute("SELECT wins FROM fighter WHERE name == 'red'")
            newWins = cursor_connection.fetchone()[0]
            assert newWins > oldWins
            assert newWins == 21
        def it_increments_the_losses_of_the_losing_fighter(test_db, red_fighter, blue_fighter, cursor_connection):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            cursor_connection.execute("SELECT losses FROM fighter WHERE name == 'red'")
            oldLoss = cursor_connection.fetchone()[0]
            db.insertFight("red", "blue", False, test_db)
            cursor_connection.execute("SELECT losses FROM fighter WHERE name == 'red'")
            newLoss = cursor_connection.fetchone()[0]
            assert newLoss > oldLoss
            assert newLoss == 21
        def it_raises_exception_if_table_does_not_exist(test_db, red_fighter, blue_fighter, no_fight_table, capsys):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            db.insertFight("red", "blue", True, test_db)
            captured = capsys.readouterr()
            assert "Table Does not exist" in captured.out

    def describe_insertRound():
        def it_adds_new_round_to_db(test_db, red_fighter, blue_fighter, cursor_connection):
            cursor_connection.execute("SELECT MAX(round_id) FROM Round")
            oldId = cursor_connection.fetchone()[0]
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertRound(1, 20, 30, test_db)
            cursor_connection.execute("SELECT MAX(round_id) FROM Round")
            newId = cursor_connection.fetchone()[0]
            if oldId is not None:
                assert newId > oldId
            else:
                assert newId == 1
        def it_raises_exception_if_table_does_not_exist(test_db, no_round_table, capsys):
            db.insertRound(0, 0, 0, test_db)
            captured = capsys.readouterr()
            assert "Table Does not exist" in captured.out

    def describe_insertTournament():
        def it_updates_winner_was_champion(test_db, red_fighter, blue_fighter, cursor_connection):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertTournament("test_tourn", "1", "2", "3", test_db)
            cursor_connection.execute("SELECT was_champion FROM fighter WHERE name == 'red'")
            was = cursor_connection.fetchall()[0][0]
            assert was == 1
        def it_inserts_champion_into_champ_table(test_db, red_fighter, blue_fighter, cursor_connection):
            db.insertFighter(*red_fighter.values(), test_db)
            db.insertFighter(*blue_fighter.values(), test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertFight("red", "blue", True, test_db)
            db.insertTournament("test_tourn", "1", "2", "3", test_db)
            cursor_connection.execute("SELECT fighter_id FROM fighter WHERE name == 'red'")
            red = cursor_connection.fetchone()[0]
            cursor_connection.execute("SELECT fighter_id FROM Champion WHERE tournament_id == 1")
            champ = cursor_connection.fetchone()[0]
            assert champ == red
        def it_raises_exception_if_table_does_not_exist(test_db, no_tournament_table, capsys):
            db.insertTournament("name", "semiA", "semiB", "finalFight", test_db)
            captured = capsys.readouterr()
            assert "Table Does not exist" in captured.out