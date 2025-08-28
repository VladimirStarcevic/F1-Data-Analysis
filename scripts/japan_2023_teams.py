import os
import csv
from typing import Dict, List, Tuple

data_folder = "data"

input_filename_race = "japan_2023_race_results.csv"
input_filename_constructors = "constructors_updated.csv"
input_path_race = os.path.join("..",data_folder, input_filename_race)
input_path_constructors = os.path.join("..", data_folder, input_filename_constructors)


output_filename = "japan_2023_rich_teams.csv"
output_path = os.path.join("..",data_folder, output_filename)


def get_constructors_info(list_from_csv: List[list]) -> Dict[str, Tuple]:
    constructor_info_dict = {}

    for data_row in list_from_csv[1:]:
        constructor_id = data_row[0]

        constructor_name = data_row[2]
        constructor_nationality = data_row[3]
        constructor_url = data_row[4]

        info_tuple = (constructor_name, constructor_nationality, constructor_url)

        constructor_info_dict[constructor_id] = info_tuple

    return constructor_info_dict

try:

    with open(input_path_constructors, 'r', encoding='utf-8') as f_constructors:

        constructors_data = list(csv.reader(f_constructors))

    with open(input_path_race, 'r', encoding='utf-8') as f_race:

        race_data = list(csv.reader(f_race))
        id_to_name_map = get_constructors_info(constructors_data)

    with open(output_path, "w", encoding='utf-8') as f_out:
        header = "constructorName,driverId,points,constructorNationality,wikipediaUrl\n"
        f_out.write(header)

        for race in race_data[1:]:
            driver_id = race[2]
            constructor_id = race[3]
            points = race[9]

            constructor_info = id_to_name_map.get(constructor_id)
            if constructor_info:
                name, nationality, url = constructor_info
                new_data_list = [name, driver_id, points, nationality, url]
                new_line = ",".join(new_data_list)
                final_line = new_line + "\n"

                f_out.write(final_line)

except FileNotFoundError as e:
    print(f"ERROR: A required file was not found.")
    print(f"Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")