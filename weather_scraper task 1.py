import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
from datetime import datetime
import re

# Define the URL
url = 'https://www.estesparkweather.net/archive_reports.php?date=202005'

# Send an HTTP GET request to the URL
page = requests.get(url)

# Check if the request was successful (status code 200)
if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Find the table elements on the webpage
    tables = soup.find_all('table')
    
    # Initialize lists to store data
    df_list = []
    
    # Process and clean data
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all('td')
            data = [re.sub(r'\s+', ' ', col.text.strip()) for col in columns]
            if len(data) > 0:
                df_list.append(data)

    # Create a DataFrame with the data
    df = pd.DataFrame(df_list)
    
    # Replace "None" with "N/A" for missing values in the entire DataFrame
    df = df.replace(to_replace='None', value='N/A')

    # Save the data in a CSV file
    with open("weather_data.csv", mode='w', newline='') as csv_file:
        fieldnames = ['Temperature', 'Humidity']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the weather data
        for row in df.itertuples(index=False):
            writer.writerow({'Temperature': row[0], 'Humidity': row[1]})

    print("Weather data has been scraped and saved to weather_data.csv")
    
else:
    print("Failed to retrieve data from the website.")

