import json
from datetime import datetime 

def weather_transform():
    """
    Load raw weather.json and transform it into a clean list of records
    """
    try:
        with open ('data/weather.json', 'r') as f:
            data = json.load(f)

        hourly = data.get('hourly', {})
        times = hourly.get('time', [])
        temps = hourly.get('temperature_2m', [])

        print(data["hourly"].keys())
        print(len(data["hourly"]["time"]))
        print(len(data["hourly"]["temperature_2m"]))

        if len(times) != len(temps):
            print("Warning: times and temps length mismatch")
            return []
        
        # Build list of dictionaries
        records = []
        for t, temp in zip(times, temps):
            # convert ISO timestamp to readable date-time
            dt = datetime.fromisoformat(t)

            records.append({
                'datetime': dt.strftime('%Y-%m-%d %H:%M'),
                'temperature': temp
            })
        print(f'Transformed {len(records)} records.')
        return records
        
    except FileNotFoundError:
        print('weather.json Not Found. Run fetch.py first')
        return []
    
if __name__ == '__main__':
    weather_transform()