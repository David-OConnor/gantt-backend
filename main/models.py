from django.db import models


class Organization(models.Model):
    id = models.IntegerField(primary_key=True)  
    name = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20)
    order = models.IntegerField()


class Event(models.Model):
    id = models.IntegerField(primary_key=True)   
    name = models.CharField(max_length=30, unique=True)
    org = models.ForeignKey(Organization, related_name='events', on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
