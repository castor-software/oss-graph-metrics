# List of all closed prs

Google BigQuery : 
```sql
 SELECT repo.name, 
    TIMESTAMP(REPLACE(JSON_EXTRACT(payload, '$.pull_request.created_at'), "\"", "")) as created_at,
    TIMESTAMP(REPLACE(JSON_EXTRACT(payload, '$.pull_request.closed_at'), "\"", "")) as closed_at,
    JSON_EXTRACT(payload, '$.pull_request.number') as pr_id,
    JSON_EXTRACT(payload, '$.pull_request.merged_at') as merged_at,
    JSON_EXTRACT(payload, '$.pull_request.merged') as merged
  FROM `tx01-234015.GHA.java_2017`
  WHERE type='PullRequestEvent'
  and JSON_EXTRACT(payload, '$.action') = "\"closed\""
```



Get the average pr close time by month by the time it is closed.

```sql
SELECT name,
  DATETIME_TRUNC(DATETIME(closed_at), MONTH) as month,
  count(pr_id) as count,
  AVG(DATETIME_DIFF(DATETIME(closed_at), DATETIME(created_at), MINUTE)) as lifespan
FROM (
  SELECT repo.name, 
    TIMESTAMP(REPLACE(JSON_EXTRACT(payload, '$.pull_request.created_at'), "\"", "")) as created_at,
    TIMESTAMP(REPLACE(JSON_EXTRACT(payload, '$.pull_request.closed_at'), "\"", "")) as closed_at,
    JSON_EXTRACT(payload, '$.pull_request.number') as pr_id,
    JSON_EXTRACT(payload, '$.pull_request.merged_at') as merged_at,
    JSON_EXTRACT(payload, '$.pull_request.merged') as merged
  FROM `tx01-234015.GHA.java_all`
  WHERE type='PullRequestEvent'
  and JSON_EXTRACT(payload, '$.action') = "\"closed\""
)
GROUP BY name, month
ORDER BY name, month
```

For a specific repo
```sql
SELECT name,
  DATETIME_TRUNC(DATETIME(closed_at), MONTH) as month,
  count(pr_id) as count,
  AVG(DATETIME_DIFF(DATETIME(closed_at), DATETIME(created_at), MINUTE)) as lifespan
FROM (
  SELECT repo.name,
    TIMESTAMP(REPLACE(JSON_EXTRACT(payload, '$.pull_request.created_at'), "\"", "")) as created_at,
    TIMESTAMP(REPLACE(JSON_EXTRACT(payload, '$.pull_request.closed_at'), "\"", "")) as closed_at,
    JSON_EXTRACT(payload, '$.pull_request.number') as pr_id,
    JSON_EXTRACT(payload, '$.pull_request.merged_at') as merged_at,
    JSON_EXTRACT(payload, '$.pull_request.merged') as merged
  FROM `tx01-234015.GHA.java_all`
  WHERE type='PullRequestEvent'
  and JSON_EXTRACT(payload, '$.action') = "\"closed\""
)
GROUP BY name, month
ORDER BY name, month
```
