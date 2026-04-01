# HEX & BINARY CODE GAME
#### Video Demo: https://www.youtube.com/watch?v=qQ07fxuFIS4
#### Description:
This project is a web based game platform featuring 4 mini games focused on color (HEX) recognition and binary/ASCII conversion. It includes user authentication and a leaderboard system to track players' performance.

#### GAME MODES
1. Hex Code Guesser, is a mini game that randomly generates a hex color and displays it on the screen. The player is given 5 different randomly generated
hex codes as options. The player must guess the hex code of the displayed color. Tracks scores and streaks.

2. Hex Color Guesser, is a mini game that has the same idea as the Hex Code Guesser's, but
in this game mode the randomly generated hex code is displayed on the screen and the options contain the colors.
The player must guess the color that corresponds to the displayed hex code. Tracks scores and streaks too.

3. Binary Guesser, is a mini game that this time displays an 8-digit binary code on the screen, and gives 5 options
which contain just a letter (lower and upper case. depending on the chosen difficulty) or a number.
The player must guess the ASCII letter that corresponds to the displayed Binary code. Tracks scores and streaks as well.

4. ASCII to Binary Code, is a mini game that has the same idea as Binary Guesser's, but
in this game mode the displayed value is a number or a letter (lower and upper case, depending on the chosen difficulty)
and the options contain Binary codes. The player must guess the Binary code that corresponds to the displayed
ASCII letter

#### Features
 -Streak & Score system: The website evaluates your progress by scoring it. Scoring is directly proportional with the streak flow.

 -Register/Login/Logout: The website also requires the user to register or login by providing a username and a password in order to keep track of the users'
 scores and streaks (for each game) and display it on a LeaderBoard that ranks the players by the highest score.

-LeaderBoard: The LeaderBoard updates everytime a player scores a higher score for each game and shows the highest score, the best streak (of the highest score)
 and the game played of every player that completed a mini game

#### Techs used
-HTML, CSS, JAVASCRIPT
-Flask
-SQL to backup registration

#### Files:
 -bash```$templates/csgame.html```: The homepages html. Luxury design. has four buttons in the header, Modes forwards to the game modes section, Leaderboard forwards
 to bash```$templates/leader.html```, Contact forwards to the footer and Logout logs the user out to the logining page.

 -bash```$templates/hex1.html```: The html for the Hex Code Guesser mini game. Its design is in bash```$static/hex1.css```

 -bash```$templates/hex2.html```: The html for the Hex Color Guesser mini game. Its design is in bash```$static/hex2.css```

 -bash```$templates/binary.html```: The html for the Binary Guesser mini game.

 -bash```$templates/binary2.html```: The html for the ASCII to Binary Code mini game.

 -bash```$templates/leader.html```: The html for the leaderboard page.

 -bash```$templates/login.html```: The html for the logining page.

 -bash```$templates/register.html```: The html for the registeration page.

 -users.db: Is the sqlite3 database where users' information is stored. Usernames, passwords and IDs are stored in a table called users;
 Scores, streaks, games played are stored in different table called scores.

#### Notes:
-the website's UI design was mostly assisted by AI tools, while all game logic and functionality were implemented by me.

-i also made a separate version of this project, that i didnt dwell on its design much, that contains the color guessing and the binary guessing game modes
coded solely by me (without ai) to demonstrate my capability. The website is shown at the end of the provided video and in bash```$project/project1```
