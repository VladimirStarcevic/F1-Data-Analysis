SELECT DISTINCT
    t.name
FROM
    teams AS t
JOIN
    winners AS w ON w.team_id = t.id
JOIN
    races AS r ON r.id = w.race_id
WHERE r.continent = 'Europe'
