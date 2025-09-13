from typing import List
from driver_results import DriverResult

race_results_data = [
    {
        "driver_name": "Max Verstappen",
        "team": "Red Bull Racing",
        "laps_completed": 58,
        "fastest_lap_time": 89.3,
        "penalties_seconds": 0
    },
    {
        "driver_name": "Charles Leclerc",
        "team": "Ferrari",
        "laps_completed": 58,
        "fastest_lap_time": 88.9,
        "penalties_seconds": 5
    },
    {
        "driver_name": "Lando Norris",
        "team": "McLaren",
        "laps_completed": 57,
        "fastest_lap_time": 89.1,
        "penalties_seconds": 0
    },
    {
        "driver_name": "Lewis Hamilton",
        "team": "Mercedes",
        "laps_completed": 58,
        "fastest_lap_time": 89.3,
        "penalties_seconds": 10
    },
    {
        "driver_name": "Sergio Perez",
        "team": "Red Bull Racing",
        "laps_completed": 58,
        "fastest_lap_time": 89.5,
        "penalties_seconds": 5
    }
]




def get_drivers_data_list(data_in: List[dict]) -> List[DriverResult]:
    if not data_in:
        return []
    drivers_list = []
    for race_result in data_in:
        drivers_list.append(DriverResult(race_result['driver_name'], race_result['team'], race_result['laps_completed'], race_result['fastest_lap_time'], race_result['penalties_seconds']))
    return drivers_list


driver_objects = get_drivers_data_list(race_results_data)
for driver in driver_objects:
    print(driver)

final_standings = sorted(driver_objects)
print("\n========== Final Result ===========")
for driver in final_standings:
    print(driver.get_name())