#!/usr/bin/env python3
import argparse

from interface import *
from populate import *

from database import *


def parseArgs():
    parser = argparse.ArgumentParser(
        prog="Compubox", description="A simple command line Compubox")
    parser.add_argument("--hint", "-hi", type=int, default=0)
    parser.add_argument("--add-fighter", "-afr", type=int, default=0)
    parser.add_argument("--add-coach", "-ac", type=int, default=0)
    parser.add_argument("--add-fight", "-af", type=int, default=0)
    parser.add_argument("--add-round", "-ar", type=int, default=0)
    parser.add_argument("--add-tournament", "-at", type=int, default=0)
    parser.add_argument("--populate", "-p", type=int, default=0)
    parser.add_argument("--interesting", "-i", type=int, default=0)

    # Test arguments here

    args = parser.parse_args()
    return args


def main(args):
    if (args.add_fighter != 0):
        addFighter(args.hint)

    if (args.add_coach != 0):
        addCoach(args.hint)

    if (args.add_fight != 0):
        addFight(args.hint)

    if (args.add_round != 0):
        addRound(args.hint)

    if (args.add_tournament != 0):
        addTournament(args.hint)

    if (args.populate != 0):
        populateFighters("../data/fighters.csv")
        populateCoaches("../data/coach.csv")
        populateFights("../data/fight.csv")
        populateRounds("../data/rounds.csv")
        populateTournaments("../data/tournament.csv")

    if (args.interesting != 0):
        getWorstCoaches()
        print("\n\n\n")
        getRobbed()


if __name__ == "__main__":
    main(parseArgs())
