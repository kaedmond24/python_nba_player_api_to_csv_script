#############################################################################################
# Created by Kevin Edmond.
#
# 
# 
#  
# 
#
# Please read README.md for full notes on script.
#
#############################################################################################

import json
import requests
import csv

# RapidAPI API Python Template
# API URL
url = "https://free-nba.p.rapidapi.com/players"
querystring = {"page":"1","per_page":"100"}

# Headers for Rapidapi authentication 
headers = {
	"X-RapidAPI-Key": "ADD RAPIDAPI KEY",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

# API call to get player data
response = requests.get(url, headers=headers, params=querystring)
# Convert API call response to JSON 
player_list = response.json()

# Get total pages of returned data 
total_pages = player_list['meta']['total_pages']
# Set page number to loop through each page of data
page = 1


# Create CSV file
# Columns: Player ID # |  First Name |  Last Name | Position | Team Name
csv_filename = "nba_players.csv"
csv_header = ["player id #", "first name" , "last name", "position", "team name"]

with open(csv_filename, "w", newline='') as file:
    # Pass in name of file being written to
    writer = csv.writer(file)
    # Write header to first row of CSV file
    writer.writerow(csv_header)
    
    # Loop through each page of API response
    # Write player data to CSV file 
    while page <= total_pages:

        # Adding player csv rows
        for player in player_list['data']:
            writer.writerow([player['id'], player['first_name'], player['last_name'], player['position'], player['team']['full_name']])

        # Increment page and update API call variables
        page += 1
        querystring = {"page":page,"per_page":"100"}
        response = requests.get(url, headers=headers, params=querystring)
        player_list = response.json()


# Notify User of CSV creation
print(f"{csv_filename} has been created.")
