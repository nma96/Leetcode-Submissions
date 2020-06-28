# Write your MySQL query statement below
SELECT w.Id
FROM Weather AS w, Weather AS weather
WHERE DATEDIFF(w.RecordDate, weather.RecordDate)=1 AND w.Temperature > weather.Temperature