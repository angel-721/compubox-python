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
    quarter_finals_a_id INTEGER NOT NULL,
    quarter_finals_b_id INTEGER NOT NULL,
    semi_finals_a_id INTEGER NOT NULL,
    semi_finals_b_id INTEGER NOT NULL,
    final_fight_id INTEGER NOT NULL,
    FOREIGN KEY (quarter_finals_a_id) REFERENCES Fight (fight_id),
    FOREIGN KEY (quarter_finals_b_id) REFERENCES Fight (fight_id),
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
    punches_r_landed INTEGER NOT NULL,
    punches_b_landed INTEGER NOT NULL,
    FOREIGN KEY (fight_id) REFERENCES Fight (fight_id),
    CHECK (round_number BETWEEN 1 AND 8)
  );

CREATE TABLE
  Champion (
    fighter_id INTEGER PRIMARY KEY NOT NULL,
    tournament_id INTEGER NOT NULL,
    title_belt_name TEXT NOT NULL,
    FOREIGN KEY (fighter_id) REFERENCES Fighter (fighter_id) ON DELETE CASCADE,
    FOREIGN KEY (tournament_id) REFERENCES Tournament (tournament_id)
  );
