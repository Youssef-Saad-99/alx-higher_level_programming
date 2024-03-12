-- display the max temperature of each state (ordered by State name).
SELECT State, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY State
ORDER BY State;
