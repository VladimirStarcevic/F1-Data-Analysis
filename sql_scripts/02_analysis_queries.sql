SELECT DISTINCT races.continent
FROM races
ORDER BY races.continent;

SELECT
    races.continent,
    count(races.name) AS number_of_races
FROM races
GROUP BY races.continent
ORDER BY number_of_races DESC;


SELECT
    t.name,
    COUNT(w.team_id) AS total_win_per_team
FROM
    teams AS t
JOIN winners as w ON t.id = w.team_id
GROUP BY t.name
ORDER BY total_win_per_team DESC;


SELECT
    d.name AS driver_name,
    COUNT(w.id) AS number_of_wins
FROM
    drivers AS d
        JOIN
    winners AS w ON d.id = w.driver_id
        JOIN
    races AS r ON w.race_id = r.id
WHERE
    EXTRACT(YEAR FROM r.race_date) >= 2000
GROUP BY
    d.name
ORDER BY
    number_of_wins DESC
LIMIT 5;

