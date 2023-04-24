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
        src_db = "../database/database.db"
        shutil.copy(src_db, DB_FILE)
        yield DB_FILE
        os.remove(DB_FILE)

    def describe_insertFighter():
        def it_adds_new_fighter_to_db(test_db):
            pass
        def it_raises_exception_if_table_does_not_exist(test_db):
            pass

    def describe_insertCoach():
        def it_adds_new_coach_to_db(test_db):
            pass
        def it_raises_exception_if_table_does_not_exist(test_db):
            pass

    def describe_insertFight():
        def it_adds_new_fight_to_db(test_db):
            pass
        def it_properly_raises_exception_when_red_fighter_id_is_not_correct(test_db):
            pass
        def it_properly_raises_exception_when_blue_fighter_id_is_not_correct(test_db):
            pass
        def it_increments_the_wins_of_the_winning_fighter(test_db):
            pass
        def it_increments_the_losses_of_the_losing_fighter(test_db):
            pass
        def it_raises_exception_if_table_does_not_exist(test_db):
            pass

    def describe_insertRound():
        def it_adds_new_round_to_db(test_db):
            pass
        def it_raises_exception_if_table_does_not_exist(test_db):
            pass