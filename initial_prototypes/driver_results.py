class DriverResult:
    driver_name: str
    team: str
    laps_completed: int
    fastest_lap: float
    penalties: int


    def __init__(self, name, team, laps_completed, fastest_lap, penalties):
        self.driver_name = name
        self.team = team
        self.laps_completed = laps_completed
        self.fastest_lap = fastest_lap
        self.penalties = penalties

    def get_name(self):
        return self.driver_name

    def get_total_race_time(self) -> float:
        base_race_time = 5220
        return float('inf') if self.laps_completed < 58 else base_race_time + self.penalties

    def __lt__(self, other) -> bool:
        return self.get_total_race_time() < other.get_total_race_time()

    def __str__(self) -> str:
        return f"{self.driver_name} ({self.team}) - Laps: {self.laps_completed}, Fastest Lap: {self.fastest_lap}s"



