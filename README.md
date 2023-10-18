# Python NBA Player API to CSV Script

---

Created By Kevin Edmond

Repository for Python NBA Player API to CSV Script: Extract NBA player data and format into a CSV File

### Instructions:

1. Install Python 3 for your system using instructions [here](https://www.python.org/downloads/).<br>

2. Install required packages.<br>

   > command: `python3 pip install requests`

3. Run the script.<br>

   > command: `python3 nba_players.py`

### Script Logic:

1. Use the RapidAPI API python template to make initial API call and retrieve data

2. Create `total_pages` and `page` variables to manage pagination in returned player data.

3. Create a CSV file with column headers, `'player id #'`, `'first name'`, `'last name'`, `'position'`, and `'team name'`, to store specific player data.

4. Run a `while loop` that continues to run until `page` equals `total_pages`. Inside of this loop a `for loop` will iterate through the page of returned data adding the specific fields of data as a row in the CSV file. Once the page of data is complete, the API call variables, `page`, `querystring`, `response`, and `player_list` are updated for the subsequent page API call.

5. A notification regarding the CSV creation is displayed.
