import requests
import csv
import datetime

# Set the base URL for the API
api_url = "https://api-open.data.gov.sg/v2/real-time/api/wind-speed"

# Define the query parameters
params = {
    "date": "2024-01-17T14:00:00"  # Change to your desired date and time
}

# Send the GET request to the API
response = requests.get(api_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    
    # Extract the wind speed readings
    stations = data['data']['stations']
    readings = data['data']['readings']
    reading_unit = data['data']['readingUnit']

    # Open a CSV file to write the data
    csv_filename = "wind_speed_data.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the headers
        writer.writerow(['Timestamp', 'Station ID', 'Station Name', 'Latitude', 'Longitude', 'Wind Speed (' + reading_unit + ')'])
        
        # Write the data rows
        for reading in readings:
            timestamp = reading['timestamp']
            for record in reading['data']:
                station_id = record['stationId']
                wind_speed_value = record['value']
                
                # Get the station information
                station_info = next((s for s in stations if s['id'] == station_id), None)
                
                if station_info:
                    station_name = station_info['name']
                    latitude = station_info['location']['latitude']
                    longitude = station_info['location']['longitude']
                    
                    # Write the row in the CSV
                    writer.writerow([timestamp, station_id, station_name, latitude, longitude, wind_speed_value])
                    
    print(f"Data successfully exported to {csv_filename}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.json())

