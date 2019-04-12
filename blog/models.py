from django.db import models

class Post(models.Model):
    class Meta:
        ordering = ('-pub_date', )

    headline = models.CharField(max_length = 100)
    entry = models.TextField(default = '')
    pub_date = models.DateField()
    image = models.ImageField(null = True,upload_to = 'images')

    def __str__(self):
        return self.headline


# Create your models here.
