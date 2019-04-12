from django.db import models
from django.contrib.auth.models import User

class Timelog(models.Model):
    person = models.ForeignKey(User, on_delete = models.CASCADE, blank = True)
    logdate = models.DateField()
    minutes = models.IntegerField()
    description = models.CharField(max_length = 300, blank = True, null = True)
    work_day = models.DateField(null = True)


    def __str__(self):
        return self.person + ' ' + self.description + ' - ' + self.description

# Create your models here.
