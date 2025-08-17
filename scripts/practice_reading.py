import os
import csv

data = "data"
file_name = "2023_race_results.csv"
file_path = os.path.join("..", data, file_name)


try:
    with open(file_path, "r", encoding = 'utf-8') as f_in:

        csv_reader = csv.reader(f_in)
        header = next(csv_reader)
        print("========== HEADER ==========")
        print(header)
        print("=" * 100)
        for row in csv_reader:
            print(row)



except FileNotFoundError:
    print(f"ERROR: File {file_name} not found")
except Exception as e:
    print(f"An error occurred: {e}")