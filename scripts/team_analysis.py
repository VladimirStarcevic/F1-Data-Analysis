import os
import csv

def count_points_by_constructor(data_list):
    constructor_points_finishes = {}
    for row in data_list[1:]:
        positon_order = int(row[8])
        if positon_order <= 10:
            constructor_id = row[3]

            if constructor_id in constructor_points_finishes:
                constructor_points_finishes[constructor_id] += 1
            else:
                constructor_points_finishes[constructor_id] = 1
    return constructor_points_finishes


data = "data"
file_name = "2023_race_results.csv"
file_path = os.path.join("..", data, file_name)


try:
    with open(file_path, "r", encoding = 'utf-8') as f_in:


        all_race_list = list(csv.reader(f_in))

        team_analysis_info = count_points_by_constructor(all_race_list)
        print(f"============ F1 Team Analysis: =================\n{team_analysis_info}")





except FileNotFoundError:
    print(f"ERROR: File {file_name} not found")
except Exception as e:
    print(f"An error occurred: {e}")