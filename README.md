# elk-markov

ELK stack project to ingest text generated from Markov chains.

I made this to learn some of the ELK stack and mess around with Markov chains a little.

## Summary

Markov => FileBeat => LogStash => ElasticSearch => Kibana

I just wanted a stream of constant junk data to pull in and explore ElasticSearch/Kibana with.

## Run

`docker compose -f docker-compose.yml up --build`

## References

- Markov chains
  - https://www.kdnuggets.com/2019/11/markov-chains-train-text-generation.html
  - https://www.nltk.org/book/ch02.html
  - https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
- ELK stack
  - https://medium.com/@sece.cosmin/docker-logs-with-elastic-stack-elk-filebeat-50e2b20a27c6
  - https://www.bogotobogo.com/DevOps/Docker/Docker_ELK_7_6_Elastic_Stack_Docker_Compose.php
  - https://github.com/deviantony/docker-elk
- https://www.gutenberg.org/files/2701/2701-h/2701-h.htm