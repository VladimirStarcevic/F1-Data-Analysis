import psycopg2
import csv
import os
from dotenv import load_dotenv


load_dotenv()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FOLDER = "data"
GRAND_PRIX_DATA = "winners_f1_1950_2025_v2.csv"
FILE_PATH = os.path.join(PROJECT_DIR, DATA_FOLDER, GRAND_PRIX_DATA)
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS")
    )
    cur = conn.cursor()

    with open(FILE_PATH, "r", encoding='UTF-8') as file_in:

        csv_reader = csv.reader(file_in)
        header = next(csv_reader)
        for row in csv_reader:

            team_name = row[5]
            race_name = row[2]
            circuit = row[3]
            continent = row[1]
            date = row[0]
            winner_name = row[4]
            winner_time = row[6]
            laps_string = row[7]
            laps_integer = int(float(laps_string))
            year = row[8]

            sql_insert_driver = """
            INSERT INTO drivers (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            RETURNING id;
            """
            cur.execute(sql_insert_driver, (winner_name,) )
            result_driver = cur.fetchone()
            driver_id = None

            if result_driver:
                driver_id = result_driver[0]
                print(f"Created new driver '{winner_name}' with ID: {driver_id}")
            else:
                sql_select_driver = "SELECT id FROM drivers WHERE name = %s;"
                cur.execute(sql_select_driver, (winner_name,))
                driver_id = cur.fetchone()[0]
                print(f"Found existing driver '{winner_name}' with ID: {driver_id}")

            sql_insert_team = """
            INSERT INTO teams (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            RETURNING id
            """
            cur.execute(sql_insert_team, (team_name,))
            result_team = cur.fetchone()
            team_id = None
            if result_team:
                team_id = result_team[0]
                print(f"Created new team '{team_name} with ID: {team_id}")
            else:
                sql_select_team = "SELECT id FROM teams WHERE name = %s;"
                cur.execute(sql_select_team, (team_name,))
                team_id = cur.fetchone()[0]
                print(f"Found existing team '{team_name} with ID: {team_id}")

            sql_insert_race = """
                INSERT INTO races (name, circuit_name, continent, race_date)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (name, race_date) DO NOTHING
                RETURNING id;
            """
            cur.execute(sql_insert_race, (race_name, circuit, continent, date))
            result_race = cur.fetchone()

            race_id = None

            if result_race:
                race_id = result_race[0]
                print(f"Created new race '{race_name}' on {date} with ID: {race_id}")
            else:
                sql_select_race = "SELECT id FROM races WHERE name = %s AND race_date = %s;"
                cur.execute(sql_select_race, (race_name, date))
                race_id = cur.fetchone()[0]
                print(f"Found existing race '{race_name}' on {date} with ID: {race_id}")

            sql_insert_winner = """
            INSERT INTO winners (driver_id, team_id, race_id, race_time, laps)
            VALUES (%s, %s, %s,%s, %s)
            RETURNING id
            """
            cur.execute(sql_insert_winner, (driver_id, team_id, race_id, winner_time, laps_integer))
            print(f"--- Inserted WINNER record for race '{race_name}' ---")




    conn.commit()
except Exception as e:
    print(f"ERROR: {e}")
    if conn:
        conn.rollback()
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()