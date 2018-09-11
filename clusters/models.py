from django.db import models


# Create your models here.
class Cluster(models.Model):
    date = models.DateField(auto_created=True)
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=50)
    node_count = models.IntegerField(default=3)

    def __str__(self):
        return self.name


