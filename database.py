import sqlite3

DB_PATH = "data/weather.db"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            datetime TEXT PRIMARY KEY,
            temperature REAL
        )
    """)

    conn.commit()
    conn.close()
    print("Table ready")


def insert_records(records):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for r in records:
        cursor.execute("""
            INSERT OR REPLACE INTO weather (datetime, temperature)
            VALUES (?, ?)
        """, (r["datetime"], r["temperature"]))

    conn.commit()
    conn.close()
    print(f"Inserted {len(records)} records into database")