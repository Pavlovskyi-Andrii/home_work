FROM fluent/fluentd:v1.16-debian-1
USER root
RUN gem install fluent-plugin-elasticsearch --no-document
COPY conf/fluent.conf /fluentd/etc/fluent.conf
USER fluent

