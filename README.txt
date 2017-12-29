## Project: Tournament Results Database

#### Codes are taken from instructors notes, github and websites.

## Project Description:

Developed a database schema to store the game matches between
players. Wrote code to query this data and determined the winners
of various games.

Wrote a Python module that uses the PostgreSQL database
to keep track of players and matches in a game tournament.
The game tournament used the Swiss system for pairing up players
in each round: players are not eliminated, and each player should be
paired with another player with the same number of wins, or as close as possible.

The goal of the Swiss pairings system is to pair each player with an 
opponent who has won the same number of matches.
Assumed that the number of players in a tournament is an even number.


Code and database only support a single tournament at a time.
When I want to run a new tournament, all the game records from the 
previous tournament will be deleted.

## Set up:
 
Vagrant from vagrantup.com.
VirtualBox from virtualbox.org. 
Git from git-scm.com.
Used Git Bash terminal.


## Code Templates:

tournament.sql, tournament.py, and tournament_test.py.
•	tournament.sql is the database schema, in the form of SQL create table commands.
•	tournament.py is where I have several functions. 
•	tournament_test.py will test the functions written in tournament.py.
•	Ran the tests using the command python tournament_test.py.

In order to get vagrant up to work, I first needed to remove the hidden .vagrant
directory. I did this with the command rm -rf .vagrant.
1. Downloaded the VM configuration directory FSND-Virtual-Machine.
2. Changed to this directory in terminal with cd/FSND-Virtual-Machine/vagrant
3. From the terminal, inside the vagrant subdirectory,run the command vagrant up.
   This will cause Vagrant to download the Linux operating system and install it.
4. Run vagrant ssh to log in to Linux VM!

Files inside VM:

1. Inside the VM, change to the /vagrant/tournament directory with the following command:
   cd /vagrant. Files in the VM's /vagrant directory are shared with the vagrant folder on
   my computer. PostgreSQL database lives inside the VM.


Created Database:

From the linux command line, type psql to enter the interactive Postgres terminal.
Enter the following command to create the tournament database:
\i tournament.sql
Exit the Postgres terminal and return to the Linux command line with the following command:
\q

tournament.sql
Created a players table -  
ex:
       id |       name
----+-------------------
        1 | Twilight Sparkle
        2 | Fluttershy
        3 | Applejack
        4 | Pinkie Pie
        5 | Rarity
        6 | Rainbow Dash
        7 | Princess Celestia
        8 | Princess Luna
      (8 rows)
			
Created results table to hold the match id's and players id's
that correspond with the winner and loser of the match.
ex:
      matchid | winner | loser
    -----------------------------
            1 |      1  |    2  |
            2 |      3  |    4  |

Created a view standings, that will be sorted by total_wins
and then by total_matches as such:
examples of newly registered players in view standings will have no
matches or wins.

    id |       name       | total_wins | total_matches
----+------------------+------------+---------------
  5 | Melpomene Murray |          0 |             0
  6 | Randy Schwartz   |          0 |             0

tournament.py

Functions:

connect() - Connect to the PostgreSQL database.  Returns a database connection.
deleteMatches() -  Removes all results records such as wins, lossses and match
id's from the database.
deletePlayers() - Remove all the player records from the database.
countPlayers() - Returns the number of players currently registered.
registerPlayer(name) - Adds a player to the tournament database.  
playerStandings() - Returns a list of the players and their win records, sorted by wins.

  
Run a project:

In the command line type: python tournament_test.py.

## Output:

1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
[(3, 'Melpomene Murray', 0L, 0L), (4, 'Randy Schwartz', 0L, 0L)]
6. Newly registered players appear in the standings with no matches.
[(5, 'Bruno Walton', 0L, 0L), (6, "Boots O'Neal", 0L, 0L), (7, 'Cathy Burton', 0                                                                                                                L, 0L), (8, 'Diane Grant', 0L, 0L)]
[(5, 'Bruno Walton', 1L, 1L), (7, 'Cathy Burton', 1L, 1L), (6, "Boots O'Neal", 0                                                                                                                L, 1L), (8, 'Diane Grant', 0L, 1L)]
7. After a match, players have updated standings.
[(5, 'Bruno Walton', 0L, 0L), (6, "Boots O'Neal", 0L, 0L), (7, 'Cathy Burton', 0                                                                                                                L, 0L), (8, 'Diane Grant', 0L, 0L)]
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
[(9, 'Twilight Sparkle', 0L, 0L), (10, 'Fluttershy', 0L, 0L), (11, 'Applejack',                                                                                                                 0L, 0L), (12, 'Pinkie Pie', 0L, 0L), (13, 'Rarity', 0L, 0L), (14, 'Rainbow Dash'                                                                                                                , 0L, 0L), (15, 'Princess Celestia', 0L, 0L), (16, 'Princess Luna', 0L, 0L)]
10. After one match, players with one win are properly paired.
Success!  All tests pass!


Exit from the database: \q
Logging out: Type exit (or Ctrl-D)
Logging in:   Type vagrant ssh

Issues:
I was having problem when I was trying to connect to the database
by typing only \c tournament.
I had to type \c tournament and then \c vagrant


License:

Database Tournament project is a course work for the Full Stack Developer program.
