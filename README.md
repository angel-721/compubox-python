# compubox-python

![Boxing statistics database](https://cdn.pixabay.com/photo/2014/04/02/14/06/matt-306160_960_720.png)

## these are a couple of the basic commands you will need

|commands: | arguments|
| -| -|
|--add-fighter|name,height,reach,wins,losses,draws,wasChampion,coachID |
|--add-coach|name|
|--add-fight|blue-name,red-name, winner|
|--add-round|fight-id,red-punch-count, blue-punch-count|
|--add-tournament|name,semiA,semiB,final-fight|
|--populate|populate database|
|--interesting|make things interesting|

## to run the tests run these commands

- you can install the dependancies required for the tests by running <code> make install </code>
- you can run all the tests by running <code> make tests </code>
- the tests check that
  - insertFighter adds a new fighter to the db
  - insertFighter raises exception an if the table does not exist
  - insertCoach adds a new coach to the db
  - insertCoach raises exception an if the table does not exist
  - insertFight adds a new fight to the db
  - insertFight raises an exception when red fighter is not correct
  - insertFight raises an exception when blue fighter is not correct
  - insertFight increments the wins of the winning fighter
  - insertFight increments the losses of the losing fighter
  - insertFight raises exception an if the table does not exist
  - insertRound adds a new round to the db
  - insertRound raises exception an if the table does not exist
  - insertTournament updates the winner as 'was_champion'
  - insertTournament inserts the champion into champion table
  - insertTournament raises exception an if the table does not exist

- You can also run commands on make 
  - ex) <code> make add-fighter </code>
