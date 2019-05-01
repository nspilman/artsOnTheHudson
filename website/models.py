from django.db import models
from people.models import Person

default_ipsum = 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?'


class Staff(models.Model):
    name = models.CharField(max_length = 100)
    title = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to = 'website/static/website/images', default='website/static/website/images/davidStaffLogo.jpg')
    bio = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.

class Education(models.Model):
    name = models.CharField(max_length = 100)
    blurb = models.CharField(max_length = 300)
    photo = models.ImageField(upload_to = 'images', default='website/static/website/images/davidStaffLogo.jpg')
    body = models.TextField(default = default_ipsum)
    url = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Events(models.Model):
    name = models.CharField(max_length = 100)
    blurb = models.CharField(max_length = 300)
    photo = models.ImageField(upload_to = 'images', default='website/static/website/images/davidStaffLogo.jpg')
    body = models.TextField(default = default_ipsum)
    url = models.CharField(max_length = 100)
    fb_url = models.CharField(max_length = 100, null = True, blank = True)
    ticket_url = models.CharField(max_length = 100,null = True, blank = True)
    location = models.CharField(max_length = 200, default = '' )
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name

class Event_signup(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    students = models.ManyToManyField(Person, blank = True, null = True)
    parent_event = models.ForeignKey(Events, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.parent_event) + ' - ' + str(self.name)

class Promotion(models.Model):
    name = models.CharField(max_length = 100)
    blurb = models.CharField(max_length = 300)
    photo = models.ImageField(upload_to = 'images', default='website/static/website/images/davidStaffLogo.jpg')
    body = models.TextField(default = default_ipsum)
    url = models.CharField(max_length = 100)
    client = models.CharField(max_length = 100)
    medialink = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    email = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100, blank = True, null = True)
    lastname = models.CharField(max_length = 100, blank = True, null = True)
    def __str__(self):
        return self.email

class Bulletin(models.Model):
    headline = models.CharField(max_length = 100)
    bulletin = models.TextField()

    def __str__(self):
        return self.headline

class Incomingmessages(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    message = models.TextField()
    sub_time = models.TimeField()
    sub_date = models.DateField()

    def __str__(self):
        return (str(self.sub_date) + ' ' +  str(self.sub_time)  + ' ' + self.name)
# Create your models here.

class Press(models.Model):
    class Meta:
        ordering = ('-pub_date', )

    headline = models.CharField(max_length = 100)
    link = models.CharField(max_length = 100)
    blurb = models.TextField(default = '')
    publication = models.CharField(max_length = 200)
    pub_date = models.DateField()
    image = models.ImageField(null = True,upload_to = 'images')

    def __str__(self):
        return self.headline

