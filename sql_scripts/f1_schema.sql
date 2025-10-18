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