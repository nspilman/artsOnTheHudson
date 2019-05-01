from django.contrib import admin
from .models import Staff, Education, Events, Contacts, Incomingmessages, Promotion, Bulletin, Event_signup, Press
from django.db import models

# Register your models here.


admin.site.register(Incomingmessages)
admin.site.register(Education)
admin.site.register(Events)
admin.site.register(Promotion)
admin.site.register(Bulletin)
admin.site.register(Staff)
admin.site.register(Event_signup)
admin.site.register(Press)


