from django.db import models
import datetime

class Project(models.Model):
    name = models.CharField(max_length = 200)
    owner = models.ForeignKey('website.Staff', on_delete = 'CASCASE')
    description = models.TextField(blank = True)
    launch_date = models.DateField(default = datetime.datetime.today)
    next_step = models.CharField(max_length = 500, blank = True)

    def __str__(self):  
        return self.name

# Create your models here.
