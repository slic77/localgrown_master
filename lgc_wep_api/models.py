#from django.db import models
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.
class User(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    first_name = columns.Text
    last_name = columns.Text
    city = columns.Text
    state = columns.Text(max_length=2)
    base_coord = columns.Integer
