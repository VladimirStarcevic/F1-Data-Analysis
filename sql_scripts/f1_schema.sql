DROP TABLE IF EXISTS winners;
DROP TABLE IF EXISTS races;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS drivers;

CREATE TABLE drivers (
                         id SERIAL PRIMARY KEY,
                         name VARCHAR(128) NOT NULL UNIQUE,
                         nationality VARCHAR(128)
);

CREATE TABLE teams (
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(128) NOT NULL UNIQUE,
                       nationality VARCHAR(128)
);

CREATE TABLE races (
                       id SERIAL PRIMARY KEY,
                       name VARCHAR(128) NOT NULL,
                       circuit_name VARCHAR(128),
                       continent VARCHAR(128),
                       race_date DATE,

                       CONSTRAINT unique_race_date UNIQUE (name, race_date)
);

CREATE TABLE winners (
                         id SERIAL PRIMARY KEY,
                         driver_id INT REFERENCES drivers(id) ON DELETE CASCADE,
                         race_id INT REFERENCES races(id) ON DELETE CASCADE,
                         team_id INT REFERENCES teams(id) ON DELETE CASCADE,
                         race_time VARCHAR(50),
                         laps INT
);



SELECT
    d.name,  -- Koristimo alias 'd' za drivers
    t.name,  -- Koristimo alias 't' za teams
    r.name,  -- Koristimo alias 'r' za races
    r.race_date -- I drugu kolonu iz 'races'
FROM
    drivers AS d -- Dajemo nadimak 'd' našoj početnoj tabeli

        JOIN winners AS w ON d.id = w.driver_id
        JOIN races AS r ON w.race_id = r.id
        JOIN teams AS t ON w.team_id = t.id;