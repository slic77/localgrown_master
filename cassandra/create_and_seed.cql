create keyspace lgc with replication = {'class':'SimpleStrategy','replication_factor':3};
use lgc;
create table users (state text, city text, name text, id uuid, primary key((state), city, name, id)) with clustering order by (city desc, name asc);
insert into users (state, city, name, id) values ('IL', 'Somewhere', 'Chris', uuid());
insert into users (state, city, name, id) values ('MO', 'Somewhere', 'Justin', uuid());