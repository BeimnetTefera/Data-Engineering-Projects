import sqlite3

DB_PATH = "data/weather.db"

def generate_report():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # total rows
        cursor.execute("SELECT COUNT(*) FROM weather")
        total = cursor.fetchone()[0]

        # stats
        cursor.execute("""
            SELECT 
                AVG(temperature),
                MIN(temperature),
                MAX(temperature)
            FROM weather
        """)
        avg_temp, min_temp, max_temp = cursor.fetchone()

        # latest record
        cursor.execute("""
            SELECT datetime, temperature 
            FROM weather
            ORDER BY datetime DESC
            LIMIT 1
        """)
        latest = cursor.fetchone()

        print("\n🌤 WEATHER REPORT")
        print("-" * 30)
        print(f"Total records : {total}")
        print(f"Average temp  : {avg_temp:.2f} °C")
        print(f"Min temp      : {min_temp:.2f} °C")
        print(f"Max temp      : {max_temp:.2f} °C")

        if latest:
            print(f"Latest record : {latest[0]} -> {latest[1]} °C")

        conn.close()

    except sqlite3.Error as e:
        print("Database error:", e)


if __name__ == "__main__":
    generate_report()