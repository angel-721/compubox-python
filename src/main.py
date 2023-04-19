#!/usr/bin/env python3
from interface import *
# from test import *
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(prog="Compubox", description="A simple command line Compubox")
    parser.add_argument("--hint", "-hi", type=int, default=0)
    parser.add_argument("--add-fighter", "-af", type=int, default=0)
    parser.add_argument("--add-coach", "-ac", type=int, default=0)

    # Test arguments here
    
    args = parser.parse_args()
    return args

def main(args):
    if(args.add_fighter != 0):
        addFighter(args.hint)

    if(args.add_coach != 0):
        addCoach(args.hint)


        









if __name__ == "__main__":
    main(parseArgs())
