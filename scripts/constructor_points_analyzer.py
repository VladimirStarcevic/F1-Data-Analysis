from typing import Dict, List
import os
import csv

def calculate_constructor_points(race_data: List) -> Dict[str, float]:
    constructor_points_dict = {}

    for race in race_data[1:]:
        constructor_id = race[3]
        constructor_points = float(race[9])

        constructor_points_dict[constructor_id] = constructor_points_dict.get(constructor_id, 0.0) + constructor_points
    return constructor_points_dict



data = "data"
file_name = "2023_race_results.csv"
file_path = os.path.join("..", data, file_name)

try:
    with open(file_path, "r", encoding= 'UTF-8') as file_in:

        csv_reader = csv.reader(file_in)
        all_race_data = list(csv_reader)
        constructor_data = calculate_constructor_points(all_race_data)
        print(constructor_data)


except FileNotFoundError:
    print(f"ERROR: File {file_name} not found")
except Exception as e:
    print(f"An error occurred: {e}")
