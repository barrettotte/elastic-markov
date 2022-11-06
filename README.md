# elastic-markov

ElasticSearch project to ingest text generated from Markov chains.

I made this to learn some of the ELK stack and mess around with Markov chains a little.

## Summary

TODO:

containers:
- markov-generator; Python, Flask
- ElasticSearch
- LogStash
- Kibana
- API with SSRT; Java, SpringBoot, ThymeLeaf

## Run

- `docker compose -f docker-compose.yml up --build`

## References

- Markov chains
  - https://www.kdnuggets.com/2019/11/markov-chains-train-text-generation.html
  - https://www.nltk.org/book/ch02.html
  - https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
- https://www.gutenberg.org/files/2701/2701-h/2701-h.htm
