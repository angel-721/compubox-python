CREATE TABLE Fighter (
    fighter_id INTEGER PRIMARY KEY,
    name TEXT,
    height INTEGER,
    reach INTEGER,
    wins INTEGER,
    losses INTEGER,
    draws INTEGER,
    was_champion BOOLEAN,
    coach_id INTEGER,
    FOREIGN KEY (coach_id) REFERENCES Coach(coach_id)
);

CREATE TABLE Coach (
    coach_id INTEGER PRIMARY KEY,
    name TEXT
);

CREATE TABLE Tournament (
    tournament_id INTEGER PRIMARY KEY,
    tournament_name TEXT,
    quarter_finals_a_id INTEGER,
    quarter_finals_b_id INTEGER,
    semi_finals_a_id INTEGER,
    semi_finals_b_id INTEGER,
    final_fight_id INTEGER,
    FOREIGN KEY (quarter_finals_a_id) REFERENCES Fight(fight_id),
    FOREIGN KEY (quarter_finals_b_id) REFERENCES Fight(fight_id),
    FOREIGN KEY (semi_finals_a_id) REFERENCES Fight(fight_id),
    FOREIGN KEY (semi_finals_b_id) REFERENCES Fight(fight_id),
    FOREIGN KEY (final_fight_id) REFERENCES Fight(fight_id)
);

CREATE TABLE Fight (
    fight_id INTEGER PRIMARY KEY,
    winner_id INTEGER,
    loser_id INTEGER,
    FOREIGN KEY (winner_id) REFERENCES Fighter(fighter_id),
    FOREIGN KEY (loser_id) REFERENCES Fighter(fighter_id)
);

CREATE TABLE Round (
    round_id INTEGER PRIMARY KEY,
    round_number INTEGER,
    fight_id INTEGER,
    punches_r_landed INTEGER,
    punches_b_landed INTEGER,
    FOREIGN KEY (fight_id) REFERENCES Fight(fight_id),
    CHECK (round_number BETWEEN 1 AND 8)
);

CREATE TABLE Champion (
    fighter_id INTEGER PRIMARY KEY,
    tournament_id INTEGER,
    title_belt_name TEXT,
    FOREIGN KEY (fighter_id) REFERENCES Fighter(fighter_id),
    FOREIGN KEY (tournament_id) REFERENCES Tournament(tournament_id)
);
