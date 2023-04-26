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

### Schema 
<pre><code> 
  CREATE TABLE
  Fighter (
    fighter_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    height INTEGER NOT NULL,
    reach INTEGER NOT NULL,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    was_champion BOOLEAN NOT NULL,
    coach_id INTEGER,
    FOREIGN KEY (coach_id) REFERENCES Coach (coach_id)
  );

CREATE TABLE
  Coach (coach_id INTEGER PRIMARY KEY, name TEXT NOT NULL);

CREATE TABLE
  Tournament (
    tournament_id INTEGER PRIMARY KEY,
    tournament_name TEXT NOT NULL,
    semi_finals_a_id INTEGER NOT NULL,
    semi_finals_b_id INTEGER NOT NULL,
    final_fight_id INTEGER NOT NULL,
    FOREIGN KEY (semi_finals_a_id) REFERENCES Fight (fight_id),
    FOREIGN KEY (semi_finals_b_id) REFERENCES Fight (fight_id),
    FOREIGN KEY (final_fight_id) REFERENCES Fight (fight_id)
  );

CREATE TABLE
  Fight (
    fight_id INTEGER PRIMARY KEY,
    winner_id INTEGER NOT NULL,
    loser_id INTEGER NOT NULL,
    FOREIGN KEY (winner_id) REFERENCES Fighter (fighter_id),
    FOREIGN KEY (loser_id) REFERENCES Fighter (fighter_id) ON DELETE CASCADE
  );

CREATE TABLE
  Round(
    round_id INTEGER PRIMARY KEY,
    round_number INTEGER NOT NULL,
    fight_id INTEGER NOT NULL,
    punches_winner_landed INTEGER NOT NULL,
    punches_loser_landed INTEGER NOT NULL,
    FOREIGN KEY (fight_id) REFERENCES Fight (fight_id),
    CHECK (round_number BETWEEN 1 AND 8)
  );

CREATE TABLE
  Champion (
    champion_id INTEGER PRIMARY KEY NOT NULL,
    fighter_id INTEGER NOT NULL,
    tournament_id INTEGER NOT NULL,
    FOREIGN KEY (fighter_id) REFERENCES Fighter (fighter_id) ON DELETE CASCADE,
    FOREIGN KEY (tournament_id) REFERENCES Tournament (tournament_id)
  );
  </code></pre>
