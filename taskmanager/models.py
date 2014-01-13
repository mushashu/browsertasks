from django.db import models

# Create your models here.


class tasktable(models.Model):
	clientsideid = models.CharField(max_length=30)
	backendid = models.CharField(max_length=30)
	taskdescription = models.TextField()
	taskduedate = models.DateField()

