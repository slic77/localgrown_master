#docker run -it --link DC1LGCN1:cassandra --rm DC1LGCN1 sh -c 'exec cqlsh "$CASSANDRA_PORT_9042_TCP_ADDR" -f /data/create_and_seed.cql'
FROM cassandra
RUN mkdir /data
COPY data/create_and_seed.cql /data/