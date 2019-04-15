# Number of releases

Google BigQuery : 
```sql
select projects.full_name,  release_count, release_dates from `tx01-234015.java_projects.projects` projects
LEFT JOIN (SELECT repo.name as repo_name, count(id) as release_count, ARRAY_AGG(JSON_EXTRACT(payload, '$.release.published_at')) as release_dates
FROM `tx01-234015.GHA.java_2018`
WHERE type='ReleaseEvent'
GROUP BY repo.name) releases
on releases.repo_name  = projects.full_name 
order by stars desc
```

For some reason many releases are missing for exemple with the repo 'elastic/elasticsearch'

- It seams to be related to the fact that the releases are not related to a branche but simply to a commit on master
- So far we get the same results with the GH API (v4)
- However all releases are visible on the website, a solution would be to scrap the website.

GitHub API (v4):

```graphql
query { 
  repository (name:"google-java-format", owner:"google"){
    owner{
      login
    },
    name,
    releases(first:100) {
      nodes{
        tagName,
        publishedAt
      }
    }
  }
}
```
