from fetch import fetch_weather
from transform import weather_transform
from database import create_table, insert_records

def main():
    # Fetch raw data
    print('Fetching weather data ....')
    fetch_weather()

    # Transform
    print('Transforming data ...')
    records = weather_transform()
    if not records:
        print('No records to insert. Exiting.')
        return
    
    # Store in database
    print('Preparing database...')
    create_table()

    print('Inserting records...')
    insert_records(records)

    print('Pipeline Completed.')

if __name__ == '__main__':
    main()