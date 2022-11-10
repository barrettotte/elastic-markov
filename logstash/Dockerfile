FROM docker.elastic.co/logstash/logstash:7.17.7

COPY config/logstash.yml /usr/share/logstash/config/logstash.yml
COPY pipeline/logstash.conf /usr/share/logstash/pipeline/logstash.conf
COPY entrypoint.sh entrypoint.sh

CMD /bin/sh entrypoint.sh