# elastic-markov

Elastic stack project to ingest text generated from Markov chains.

I made this to learn some of the Elastic stack and mess around with Markov chains a little.
A lot of this is still a mystery to me, but I hope I can use this as a barebone reference to play around with.

## Summary

Markov.stdout => FileBeat => LogStash => ElasticSearch <= Kibana

- **Markov** outputs random sentences to stdout. The random sentences are generated via Markov chains trained on all sentences from Moby Dick
- **FileBeat** ingests all stdout/stderr from all containers in network and sends to LogStash
- **LogStash** accepts FileBeat input, processes it, and pushes to ElasticSearch
- **ElasticSearch** stores and indexes data
- **Kibana** provides visualization into ElasticSearch data and other things

## Run

`docker compose -f docker-compose.yml up --build` or `./start.sh`

## Kibana

I won't remember where some of this stuff is...

- Home - http://localhost:5601
- Index Management - http://localhost:5601/app/management/data/index_management/indices
- Dev tools - http://localhost:5601/app/dev_tools#/console

## References

- Markov chains
  - https://www.kdnuggets.com/2019/11/markov-chains-train-text-generation.html
  - https://www.nltk.org/book/ch02.html
  - https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
- Elastic stack
  - https://www.youtube.com/watch?v=Hqn5p67uev4
  - https://medium.com/@sece.cosmin/docker-logs-with-elastic-stack-elk-filebeat-50e2b20a27c6
  - https://www.bogotobogo.com/DevOps/Docker/Docker_ELK_7_6_Elastic_Stack_Docker_Compose.php
  - https://github.com/deviantony/docker-elk
  - https://www.youtube.com/playlist?list=PL_mJOmq4zsHZYAyK606y7wjQtC0aoE6Es
  - https://www.javainuse.com/elasticsearch/filebeat-elk
- https://www.gutenberg.org/files/2701/2701-h/2701-h.htm