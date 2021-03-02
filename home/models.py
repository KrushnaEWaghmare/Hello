
from datetime import datetime
# Create your models here.
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)
    comment = models.TextField(blank=True)
    hire_date = models.DateTimeField(default=datetime.now,blank=True,)

    def __str__(self):
        return 'Message from' ' : ' + self.name + '-' +self.email
    