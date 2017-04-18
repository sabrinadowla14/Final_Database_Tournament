#!/usr/bin/env python

# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        return psycopg2.connect("dbname=tournament")
    except psycopg2.Error:
        print "Cannot connect to the database"


def deleteMatches():
    """Removes all results records such as wins, lossses and match
       id's from the database."""
    db = connect()
    c = db.cursor()
    query = ("DELETE FROM results;")
    c.execute(query)
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    query = ("DELETE FROM players;")
    c.execute(query)
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""

    db = connect()
    c = db.cursor()
    query = ("SELECT count(players.id) AS count_player FROM players;")
    c.execute(query)
    count_player = c.fetchone()[0]
    db.close()
    return count_player


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by SQL database schema, not in  Python code.)
    Args:
      name: the player's full name (need not be unique). Returns the
      id number.
      ex:
       id |       name
      ----+------------------
        5 | Melpomene Murray
        6 | Randy Schwartz
        7 | Bruno Walton
        8 | Boots O'Neal
        9 | Cathy Burton
       10 | Diane Grant
      (6 rows)

    """
    query = ("INSERT INTO players(id, name) VALUES (default, %s);")
    db = connect()
    c = db.cursor()
    c.execute(query, (name,))

    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,
    or a player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played,
        collects the data as a list and returns it.
    """
    db = connect()
    c = db.cursor()
    query = ("SELECT * FROM standings;")
    c.execute(query)
    matches = c.fetchall()
    print(matches)
    db.close()
    return matches


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      postgresql commands executed by the
      cursor object which inserts a player name and id as winner
      and loser, into the results table.
    """
    db = connect()
    c = db.cursor()
    query = ("INSERT INTO results(matchId, winner, loser) \
              VALUES (default, %s, %s);")
    c.execute(query, (winner, loser,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name

        The postgresql commands to be executed by the
        cursor object which collects a list of players tuples ordered
        by total_wins column.

       'listOfPairWin' stores the list returned by cursor execution.

       The if statement will check an even number of players.
       The 'for' loop will loop over the list of tuples for the
       length of the list, where step == 2.

      'listOfPairWin' is assigned the value of 1st and 3rd,
      2nd and 4th players to create a list of at least two player pairings.
      example:
            listOfPairWin[i][0]:   player 1,3 ids
            listOfPairWin[i][1]:   player 1,3 names
            listOfPairWin[i+1][0]: player 2,4 ids
            listOfPairWin[i+1][1]: player 2,4 names
    """
    list_pair = []

    db = connect()
    c = db.cursor()
    query = ("SELECT id, name \
                FROM standings ORDER BY total_wins DESC;")
    c.execute(query)
    listOfPairWin = c.fetchall()

    if len(listOfPairWin) % 2 == 0:
        for i in range(0, len(listOfPairWin), 2):
            listOfPlayersInPair = listOfPairWin[i][0], listOfPairWin[i][1], \
                              listOfPairWin[i+1][0], listOfPairWin[i+1][1]
            list_pair.append(listOfPlayersInPair)
        

    else:
        raise ValueError('You need to have even number of players!')
        

    db.close()
    return list_pair
