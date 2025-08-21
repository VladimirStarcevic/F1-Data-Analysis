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



def map_ids_to_names(scores_dict: Dict[str, float], constructors_data: List[list]) -> Dict[str, float]:
    id_to_name_map = {}

    for row in constructors_data[1:]:
        constructor_id = row[0]
        constructor_name = row[2]

        id_to_name_map[constructor_id] = constructor_name

    named_scores = {}
    for team_id, points in scores_dict.items():
        team_name = id_to_name_map.get(team_id)

        if team_name:
            named_scores[team_name] = points
    return named_scores



data = "data"
file_name_race = "2023_race_results.csv"
file_name_constructors = "constructors.csv"
file_path_race = os.path.join("..", data, file_name_race)
file_path_constructors = os.path.join("..", data, file_name_constructors)

try:
    with open(file_path_race, "r", encoding= 'UTF-8') as file_in:

        csv_reader = csv.reader(file_in)
        all_race_data = list(csv_reader)
    with open(file_path_constructors, "r", encoding= 'UTF-8') as file_in:

        scores_by_id = calculate_constructor_points(all_race_data)

        csv_read = csv.reader(file_in)
        all_constructors_data = list(csv_read)


        id_names_map = map_ids_to_names(scores_by_id, all_constructors_data)
        for item in id_names_map.items():
            print(item)





except FileNotFoundError:
    print(f"ERROR: File {file_name_race} not found")
except Exception as e:
    print(f"An error occurred: {e}")
