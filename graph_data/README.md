# GitHub Graph Data

This folder contains different graphs (raw data and/or graphical representation) extracted from the [GHArchive](https://www.gharchive.org/) database.
The graph visualizations are made with [Gephi](https://gephi.org/).

## Structure 
The folder is orgonised as following :

  - data source
    - graph name
      - periode
        - data.csv
        - graph.csv
        - graph.pdf

## Graphs

To reduce the scope the repo are only the top 1000 Java projects in terms of stars (list available [here](./projects.csv)).

### repo_developer

(repo)<--[number of contributions]--(user)

SQL query :
```SQL
select repo_name, login, contributions from `tx01-234015.java_projects.stars` stars join (
SELECT p.repo.name as repo_name, actor.login as login, count(id) as contributions
FROM `githubarchive.month.201801` p
where date(created_at) between date('2018-01-01')
                         and date('2018-02-01')
and type in ('PullRequestReviewCommentEvent','IssueCommentEvent', 'PullRequestEvent', 'CommitCommentEvent', 'PullRequestEvent', 'PullRequestReviewEvent')
group by repo.name, actor.login
) on repo_name = stars.name
order by contributions desc
```

Yet, a contribution is described as an event of one of the following [GitHub event type](https://developer.github.com/v3/activity/events/types/) :
  - PullRequestReviewCommentEvent
  - IssueCommentEvent
  - PullRequestEvent
  - CommitCommentEvent
  - PullRequestEvent
  - PullRequestReviewEvent

### co_contributors

This graph is based on the repo_developer graph.

(repo)<--[number of contributions]--(user)

SQL query :
```SQL
SELECT name as repo1, t2.name2 as repo2, count(login) as contributors FROM `tx01-234015.GHA.contributions_201801` t1
join ( SELECT name as name2, login as login2 FROM `tx01-234015.GHA.contributions_201801` ) t2
on login = t2.login2
WHERE name <> name2
GROUP BY repo1, repo2
order by contributors desc
```
