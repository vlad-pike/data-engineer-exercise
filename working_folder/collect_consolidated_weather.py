import requests
import json
import csv

def get_consolidated_weather(woeid):
    api_url_base = 'https://www.metaweather.com/api'
    headers = {'Content-Type': 'application/json'}
    api_url = f'{api_url_base}/location/{woeid}/'

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200: #the request has succeeded
        return json.loads(response.content.decode('utf-8'))['consolidated_weather']
    else:
        return None

def upload_to_csv(location, csvheader, csvrows):
    with open(f'working_folder\consolidated_weather_{location}.csv', 'w', newline='') as csvfile:
        csvwriter = csv.DictWriter(csvfile, fieldnames=csvheader)

        csvwriter.writeheader()
        for csvrow in csvrows:
            csvwriter.writerow(csvrow)


if __name__ == '__main__':
    woeids = {'london': 44418, 'toronto': '4118', 'kiev' : 924938}

    csvheader = ['id', 'weather_state_name', 'weather_state_abbr', 'wind_direction_compass',
                 'created', 'applicable_date',
                 'min_temp', 'max_temp', 'the_temp',
                 'wind_speed', 'wind_direction',
                 'air_pressure', 'humidity', 'visibility', 'predictability']

    for location, woeid in woeids.items():
        csvrows = get_consolidated_weather(woeid)
        upload_to_csv(location, csvheader, csvrows)
