from django.db import models

# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 200)
    date = models.DateField(blank = True, null = True)

    def __str__(self):
        try:
            if date:
                return str(self.name) + " " + str(self.date)
        except:
            return self.name

class Photo(models.Model):
    name = models.CharField(max_length = 100, blank = True, null = True)
    photo = models.ImageField(upload_to = 'images')
    description = models.CharField(max_length = 200)
    date = models.DateField(blank = True, null = True)
    album = models.ManyToManyField(Album)

    def __str__(self):
        try:
            if date:
                return str(self.name) + " " + str(self.date)
        except:
            return self.name
    
class Video(models.Model):
    name = models.CharField(max_length = 100, blank = True, null = True)
    file = models.FileField(upload_to = 'video',max_length = 200)