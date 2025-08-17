import os
import csv

def calculate_wins_from_data(data_list, drivers_id):
    count_wins = 0
    for row in data_list[1:]:
        if len(row) > 6 and row[2] == drivers_id and row[6] == "1":
            count_wins += 1

    return count_wins

data = "data"
file_name = "2023_race_results.csv"
file_path = os.path.join("..", data, file_name)

try:
    with open(file_path, "r", encoding = 'utf-8') as f_in:

        all_race_data = list(csv.reader(f_in))

        max_wins = calculate_wins_from_data(all_race_data, "830")
        perez_wins = calculate_wins_from_data(all_race_data, "815")

        print(f"Number of wins for Max Verstappen (ID 830): {max_wins}")
        print(f"Number of wins for Sergio Perez (ID 815): {perez_wins}")

except FileNotFoundError:
    print(f"ERROR: File {file_name} not found")
except Exception as e:
    print(f"An error occurred: {e}")
