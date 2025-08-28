import os
import csv

data_folder = "data"

input_filename = "japan_2023_race_results.csv"
input_path = os.path.join("..",data_folder, input_filename)

output_filename = "japan_2023_drivers.csv"
output_path = os.path.join("..",data_folder, output_filename)

try:

    with open(input_path, "r", encoding='utf-8') as f_in:
        with open(output_path, "w", encoding='utf-8') as f_out:

            csv_reader = csv.reader(f_in)
            header = next(csv_reader)

            f_out.write("driverId,position\n")

            for row in csv_reader:
                driver_id = row[2]
                position = row[6]

                new_line_to_write = f"{driver_id},{position}\n"

                f_out.write(new_line_to_write)

    print(f"File '{output_filename}' created successfully.")

except FileNotFoundError:
    print(f"ERROR: File {input_filename} not found!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")