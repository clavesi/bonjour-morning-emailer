# Bonjour - Morning Newsletter
A newsletter which automatically emails you a list of interesting facts, an educational SciShow educational video, a photo from NASA, and the top news from Reuters.

*Read this in: [Français](README.fr.md)*

## How It Works
The program scrapes the web for:
- A word of the day
- The newest SciShow video
- A fun fact
- A person born on this day
- A photo from NASA
- An event that happened on this day
- Top stories from Reuters

then it updates a spreadsheet and sends an email back with all the information

## Directory Guide
- main.py (main file to run everything)
- scraper.py (scrapes the web for all the info)
- spreadsheet.py (fills out a spreadsheet with scraper.py's info)
- html_changer.py (changes the html file to send as email)
- email_server.py (sends the email)
- settings.py (file to place email information and sheet to access)
- client_secret.json (file that verifies and allows access to spreadsheet)

### How to Use
1. Install selenium's [drivers](https://selenium-python.readthedocs.io/installation.html)
2. Get rid of _sample in the client_secret.json and settings.py names.
3. Enable Google's Drive and Sheets API from their [API console](https://console.developers.google.com/apis/dashboard)
4. Create credentials for the Sheets API and paste into client_secret.json
5. Fill out settings.py
6. Run main.py

### Packages
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [selenium](https://pypi.org/project/selenium/)
- [gspread](https://pypi.org/project/gspread/)
- [oauth2client](https://pypi.org/project/oauth2client/)