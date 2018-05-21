# Competitive Coder Bot
Telegram bot to stay updated with upcoming contests on competitive coding platforms like Codechef and Hackerrank.
You can talk to the bot now at t.me/compcoderbot.

*Note:* This bot is deployed on Heroku and so it may take while (around 30s) to respond.

## Commands
This section describes the commands and parameters to use various features of the bot. All commands are case insensitive.


| Command     | Parameters   | RETURNS                                  |
|-------------|--------------|------------------------------------------|
| /start      |              | Details of all commands                  |
| /codechef   |              | Present and upcoming Codechef contests   |
| codechef    |              | Present and upcoming Codechef contests   |
| /hackerrank |              | Present and upcoming Hackerrank contests |
| hackerrank  |              | Present and upcoming Hackerrank contests |
| codechef    | Username     | Codechef profile of the user             |
| hackerrank  | Username     | Hackerrank profile of the current user   |


## TODOS
This section contains all the ideas and features I am currently working on adding
### Functionality
- [x] Show upcoming Codeforces contests
- [x] Show upcoming Hackerearth contests
- [x] Add profile scrapers for Hackerrank
- [x] Add profile scrapers for Codeforces
- [x] Add profile scrapers for Hackerearth
- [x] Show a user's rank in a currently running contest
- [x] Integrate Google's Dialogflow to enable more organic conversations
- [x] Add support for Capture The Flag competitions from [CTFTime](https://ctftime.org/)

### Deployment
- [x] Add a Heroku scheduler job to find and save the upcoming contests on regular basis
- [x] Deploy the bot to a Digital Ocean VPS