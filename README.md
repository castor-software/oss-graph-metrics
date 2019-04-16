# oss-graph-metrics
Tools to mine and compute metrics on OSS software.

## Content of the repository

This repository is organized as follows:

- [data_analysis](./data_analysis) contains queries to get various information regarding the repositories, the data itself, and some analysis carried on notebooks.
- [graph_data](./graph_data) contains some graphs extracted from GHArchive.
- [gha2sql](./gha2sql) is a small python script to get events from GHArchive and later to include them in another database.
- [maven-central-diversity](./maven-central-diversity) contains resources from the paper [The Emergence of Software Diversity in Maven Central](https://arxiv.org/abs/1903.05394).

Each directory contains its own Readme explaining its own internal organization.

## Resources

### Academic papers

- [Identifying Experts in Software Libraries and Frameworks among GitHub Users](<https://arxiv.org/abs/1903.08113>) (Joao Eduardo Montandon, Luciana Lourdes Silva, Marco Tulio Valente), MSR19
- [The Emergence of Software Diversity in Maven Central](https://arxiv.org/abs/1903.05394) (César Soto-Valero, Amine Benelallam, Nicolas Harrand, Olivier Barais, Benoit Baudry), MSR19

### Softwares

- [source{d} Engine](<https://github.com/src-d/engine>) : Powerful language-agnostic analysis of your source code and git history.
- [Reaper](https://github.com/RepoReapers/reaper) : Calculate the score of a repository based on best engineering practices.

### Data Source 

- [GH Archive](https://www.gharchive.org/) : record the public GitHub timeline, archive it, and make it easily accessible for further analysis.
- [GHTorrent](http://ghtorrent.org/) : 


## License

The content of this repository is licensed under the MIT terms.