-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE IF NOT EXISTS tournament;

CREATE DATABASE tournament;

-- Connect to the newly created database
\c tournament;


/*
Registry of player id's and their names
*/


CREATE TABLE IF NOT EXISTS players (
    id serial PRIMARY KEY,
    name text
);

/*
Creates results table to hold the match id's and players id's
that correspond with the winner and loser of the match.
*/


CREATE TABLE IF NOT EXISTS results (
        matchId serial PRIMARY KEY,
        winner integer REFERENCES players(id) NOT NULL,
        loser integer REFERENCES players(id) NOT NULL
);

/*
Creates a view standings table, that will be sorted by total_wins
and then by total_matches as such:
examples of newly registered players in view standings will have no
matches or wins.    
*/

CREATE VIEW standings AS
SELECT players.id, players.name,
(SELECT count(results.winner)
    FROM results
    WHERE players.id = results.winner)
    AS total_wins,
(SELECT count(results.matchId)
    FROM results
    WHERE players.id = results.winner
    OR players.id = results.loser)
    AS total_matches
FROM players
ORDER BY total_wins DESC, total_matches DESC;



