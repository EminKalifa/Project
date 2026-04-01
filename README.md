# HEX & BINARY CODE GAME

#### Video Demo: https://www.youtube.com/watch?v=qQ07fxuFIS4

#### Description:

 This project is a web based game platform featuring 4 mini games focused on color (HEX) recognition and binary/ASCII conversion. It includes user authentication and a leaderboard system to track players’ performance.

#### GAME MODES

 1. Hex Code Guesser is a mini game that randomly generates a hex color and displays it on the screen. The player is given 5 different randomly generated
 hex codes as options. The player must guess the hex code of the displayed color. Tracks scores and streaks.

 2. Hex Color Guesser is a mini game that has the same idea as the Hex Code Guesser’s, but
 in this game mode, the randomly generated hex code is displayed on the screen, and the options contain the colors.
 The player must guess the color that corresponds to the displayed hex code. Tracks scores and streaks too.

 3. Binary Guesser is a mini game that this time displays an 8-digit binary code on the screen, and gives 5 options
 which contain just a letter (lower and upper case, depending on the chosen difficulty) or a number.
 The player must guess the ASCII letter that corresponds to the displayed Binary code. Tracks scores and streaks as well.

 4. ASCII to Binary Code is a mini game that has the same idea as Binary Guesser’s, but
 in this game mode, the displayed value is a number or a letter (lower and upper case, depending on the chosen difficulty)
 and the options contain Binary codes. The player must guess the Binary code that corresponds to the displayed
 ASCII letter

#### Features

 -Streak & Score system: The website evaluates your progress by scoring it. Scoring is directly proportional to the streak flow.

 -Register/Login/Logout: The website also requires the user to register or log in by providing a username and a password in order to keep track of the users’
 scores and streaks (for each game) and display them on a LeaderBoard that ranks the players by the highest score.

 -LeaderBoard: The LeaderBoard updates every time a player scores a higher score for each game and shows the highest score, the best streak (of the highest score)
 and the game played by every player who completed a mini game

#### Techs used

 -HTML, CSS, JAVASCRIPT
 -Flask
 -SQL to backup registration

Files:

-```$templates/csgame.html```: The homepage HTML. Luxury design. has four buttons in the header: Modes forwards to the game modes section, Leaderboard forwards
to ```$templates/leader.html```, Contact forwards to the footer, and Logout logs the user out to the login page.

-```$templates/hex1.html```: The HTML for the Hex Code Guesser mini game. Its design is in ```$static/hex1.css```

-```$templates/hex2.html```: The HTML for the Hex Color Guesser mini game. Its design is in ```$static/hex2.css```

-```$templates/binary.html```: The HTML for the Binary Guesser mini game.

-```$templates/binary2.html```: The HTML for the ASCII to Binary Code mini game.

-```$templates/leader.html```: The HTML for the leaderboard page.

-```$templates/login.html```: The HTML for the login page.

-```$templates/register.html```: The HTML for the registration page.

-users.db: Is the SQLite3 database where users’ information is stored. Usernames, passwords, and IDs are stored in a table called users.
Scores, streaks, and games played are stored in a different table called scores.

#### Project’s Purpose

This project was created to combine learning and entertainment by turning fundamental computer science concepts into fun, interactive challenges.
Topics such as hexadecimal color and binary to ASCII conversion are often difficult for beginners to fully grasp. By turning these concepts
into mini games, the project aims to reinforce understanding through repetition, pattern recognition, and engagement rather than passive memorization.
The goal is to make abstract concepts more intuitive and approachable.

#### What I Learned

Through this project, I gained a deeper understanding of how web applications integrate frontend and backend components. I improved my skills in
Flask routing and database interaction using SQL.

I also developed a better understanding of design, particularly how visual feedback and interactivity can improve engagement. Finally, I learned how to develop a multi-feature application and maintain clean, modular code.

### Notes:

-The website’s UI design was mostly assisted by AI tools, while all game logic and functionality were implemented by me.

-I also made a separate version of this project, which I didn't dwell on its design much, that contains the color guessing and the binary guessing game modes
coded solely by me (without AI) to demonstrate my capability. The website is shown at the end of the provided video and in the ```$project/project1```
