from django.db import models
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


# Create your models here.
class Users(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text()
    city = columns.Text()
    state = columns.Text(max_length=2)
    # base_coord = columns.Integer
# create table users (state text, city text, name text, id uuid, primary key((state), city, name, id))
# with clustering order by (city desc, name asc);
